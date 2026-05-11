# Databricks notebook source
# Notebook: 005 - Atividade Pratica - Lakehouse - Gold

# COMMAND ----------

# MAGIC %md
# MAGIC ## Gold
# MAGIC
# MAGIC Cria dimensões e fato para análise do mercado de trabalho em IA.

# COMMAND ----------

from pyspark.sql import functions as F
from pyspark.sql.window import Window

df = spark.read.table("workspace.silver.ai_job_market_insights")

# COMMAND ----------

def adicionar_sk(df_dim, coluna_sk, colunas_ordem):
    janela = Window.orderBy(*[F.col(c) for c in colunas_ordem])
    return df_dim.withColumn(coluna_sk, F.row_number().over(janela)).select(coluna_sk, *df_dim.columns)

# COMMAND ----------

dim_cargo = (
    df
    .select("job_title", "required_skills", "automation_risk", "job_growth_projection")
    .dropDuplicates()
)
dim_cargo = adicionar_sk(dim_cargo, "sk_cargo", ["job_title", "required_skills", "automation_risk", "job_growth_projection"])

(
    dim_cargo.write
    .format("delta")
    .mode("overwrite")
    .option("overwriteSchema", "true")
    .saveAsTable("workspace.gold.dim_cargo")
)

# COMMAND ----------

dim_empresa = (
    df
    .select("industry", "company_size", "ai_adoption_level")
    .dropDuplicates()
)
dim_empresa = adicionar_sk(dim_empresa, "sk_empresa", ["industry", "company_size", "ai_adoption_level"])

(
    dim_empresa.write
    .format("delta")
    .mode("overwrite")
    .option("overwriteSchema", "true")
    .saveAsTable("workspace.gold.dim_empresa")
)

# COMMAND ----------

dim_localidade = (
    df
    .select("location", "remote_friendly")
    .dropDuplicates()
)
dim_localidade = adicionar_sk(dim_localidade, "sk_localidade", ["location", "remote_friendly"])

(
    dim_localidade.write
    .format("delta")
    .mode("overwrite")
    .option("overwriteSchema", "true")
    .saveAsTable("workspace.gold.dim_localidade")
)

# COMMAND ----------

fato_mercado_ia = (
    df.alias("f")
    .join(dim_cargo.alias("c"), ["job_title", "required_skills", "automation_risk", "job_growth_projection"], "inner")
    .join(dim_empresa.alias("e"), ["industry", "company_size", "ai_adoption_level"], "inner")
    .join(dim_localidade.alias("l"), ["location", "remote_friendly"], "inner")
    .select(
        F.col("f.id_linha"),
        F.col("c.sk_cargo"),
        F.col("e.sk_empresa"),
        F.col("l.sk_localidade"),
        F.col("f.salary_usd"),
        F.lit(1).alias("qtde_oportunidades"),
        F.current_timestamp().alias("data_hora_gold"),
    )
)

(
    fato_mercado_ia.write
    .format("delta")
    .mode("overwrite")
    .option("overwriteSchema", "true")
    .saveAsTable("workspace.gold.fato_mercado_ia")
)

# COMMAND ----------

# MAGIC %sql
# MAGIC SHOW TABLES IN workspace.gold;

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT
# MAGIC   c.job_title,
# MAGIC   e.industry,
# MAGIC   l.location,
# MAGIC   ROUND(AVG(f.salary_usd), 2) AS media_salarial_usd,
# MAGIC   SUM(f.qtde_oportunidades) AS qtde_oportunidades
# MAGIC FROM workspace.gold.fato_mercado_ia f
# MAGIC INNER JOIN workspace.gold.dim_cargo c
# MAGIC   ON f.sk_cargo = c.sk_cargo
# MAGIC INNER JOIN workspace.gold.dim_empresa e
# MAGIC   ON f.sk_empresa = e.sk_empresa
# MAGIC INNER JOIN workspace.gold.dim_localidade l
# MAGIC   ON f.sk_localidade = l.sk_localidade
# MAGIC GROUP BY c.job_title, e.industry, l.location
# MAGIC ORDER BY media_salarial_usd DESC;
