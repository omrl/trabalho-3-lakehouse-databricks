# Databricks notebook source
# Notebook: 003 - Atividade Pratica - Lakehouse - Bronze

# COMMAND ----------

# MAGIC %md
# MAGIC ## Bronze
# MAGIC
# MAGIC Lê os arquivos JSON gerados pela extração do MongoDB Atlas na Landing, adiciona metadados de processamento e grava cada arquivo como tabela Delta no schema `workspace.bronze`.

# COMMAND ----------

caminho_landing = "/Volumes/workspace/landing/dados"

arquivos = {
    "job_title": "job_title.json",
    "industry": "industry.json",
    "company_size": "company_size.json",
    "location": "location.json",
    "ai_adoption_level": "ai_adoption_level.json",
    "automation_risk": "automation_risk.json",
    "required_skills": "required_skills.json",
    "salary_usd": "salary_usd.json",
    "remote_friendly": "remote_friendly.json",
    "job_growth_projection": "job_growth_projection.json",
}

# COMMAND ----------

display(dbutils.fs.ls(caminho_landing))

# COMMAND ----------

from pyspark.sql.functions import current_timestamp, lit

for nome_tabela, nome_arquivo in arquivos.items():
    caminho_arquivo = f"{caminho_landing}/{nome_arquivo}"

    df = (
        spark.read
        .option("multiLine", "false")
        .json(caminho_arquivo)
        .withColumn("data_hora_bronze", current_timestamp())
        .withColumn("nome_arquivo", lit(nome_arquivo))
    )

    (
        df.write
        .format("delta")
        .mode("overwrite")
        .option("overwriteSchema", "true")
        .saveAsTable(f"workspace.bronze.{nome_tabela}")
    )

# COMMAND ----------

# MAGIC %sql
# MAGIC SHOW TABLES IN workspace.bronze;

# COMMAND ----------

# MAGIC %sql
# MAGIC DESCRIBE DETAIL workspace.bronze.job_title;
