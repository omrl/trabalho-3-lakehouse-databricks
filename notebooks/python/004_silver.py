# Databricks notebook source
# Notebook: 004 - Atividade Pratica - Lakehouse - Silver

# COMMAND ----------

# MAGIC %md
# MAGIC ## Silver
# MAGIC
# MAGIC Lê as tabelas Bronze, aplica regras de qualidade, padroniza os campos e remonta a base original usando `id_linha`.

# COMMAND ----------

from functools import reduce
from pyspark.sql import functions as F

tabelas = {
    "job_title": "Job_Title",
    "industry": "Industry",
    "company_size": "Company_Size",
    "location": "Location",
    "ai_adoption_level": "AI_Adoption_Level",
    "automation_risk": "Automation_Risk",
    "required_skills": "Required_Skills",
    "salary_usd": "Salary_USD",
    "remote_friendly": "Remote_Friendly",
    "job_growth_projection": "Job_Growth_Projection",
}

def normalizar_coluna(nome):
    return nome.lower()

def ler_e_tratar_tabela(nome_tabela, coluna_origem):
    coluna_destino = normalizar_coluna(coluna_origem)

    df = spark.read.table(f"workspace.bronze.{nome_tabela}")

    df = (
        df
        .select(
            F.col("id_linha").cast("int").alias("id_linha"),
            F.trim(F.col(coluna_origem).cast("string")).alias(coluna_destino),
        )
        .filter(F.col("id_linha").isNotNull())
        .dropDuplicates(["id_linha"])
        .withColumn("data_hora_silver", F.current_timestamp())
        .withColumn("nome_tabela_bronze", F.lit(nome_tabela))
    )

    if coluna_destino == "salary_usd":
        df = df.withColumn("salary_usd", F.col("salary_usd").cast("double"))
        df = df.filter(F.col("salary_usd").isNull() | (F.col("salary_usd") >= 0))

    (
        df.write
        .format("delta")
        .mode("overwrite")
        .option("overwriteSchema", "true")
        .saveAsTable(f"workspace.silver.{nome_tabela}")
    )

    return df.select("id_linha", coluna_destino)

# COMMAND ----------

dataframes = [
    ler_e_tratar_tabela(nome_tabela, coluna_origem)
    for nome_tabela, coluna_origem in tabelas.items()
]

df_unificado = reduce(lambda left, right: left.join(right, on="id_linha", how="inner"), dataframes)

df_unificado = (
    df_unificado
    .filter(F.col("job_title").isNotNull())
    .filter(F.col("industry").isNotNull())
    .filter(F.col("salary_usd").isNotNull())
    .withColumn("remote_friendly", F.upper(F.col("remote_friendly")))
    .withColumn("ai_adoption_level", F.upper(F.col("ai_adoption_level")))
    .withColumn("automation_risk", F.upper(F.col("automation_risk")))
    .withColumn("job_growth_projection", F.upper(F.col("job_growth_projection")))
    .withColumn("data_hora_silver", F.current_timestamp())
)

(
    df_unificado.write
    .format("delta")
    .mode("overwrite")
    .option("overwriteSchema", "true")
    .saveAsTable("workspace.silver.ai_job_market_insights")
)

# COMMAND ----------

display(df_unificado)

# COMMAND ----------

# MAGIC %sql
# MAGIC SHOW TABLES IN workspace.silver;

# COMMAND ----------

# MAGIC %sql
# MAGIC DESCRIBE DETAIL workspace.silver.ai_job_market_insights;
