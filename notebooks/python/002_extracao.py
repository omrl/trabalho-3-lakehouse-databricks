# Databricks notebook source
# Notebook: 002 - Atividade Pratica - Lakehouse - Extracao

# COMMAND ----------

# MAGIC %md
# MAGIC ## Extração
# MAGIC
# MAGIC Lê todas as collections do MongoDB Atlas e grava cada collection como JSON no volume `workspace.landing.dados`.
# MAGIC
# MAGIC A connection string não deve ser versionada no GitHub. Informe o valor no widget `mongodb_uri` ao executar o notebook no Databricks.

# COMMAND ----------

# MAGIC %pip install pymongo certifi

# COMMAND ----------

dbutils.widgets.text("mongodb_uri", "", "MongoDB Atlas URI")
dbutils.widgets.text("mongodb_database", "ai_job_market", "MongoDB Database")

mongodb_uri = dbutils.widgets.get("mongodb_uri")
mongodb_database = dbutils.widgets.get("mongodb_database")

if not mongodb_uri:
    raise ValueError("Informe a connection string do MongoDB Atlas no widget 'mongodb_uri'.")

# COMMAND ----------

import json
from pathlib import Path
import certifi
from pymongo import MongoClient

caminho_landing = "/Volumes/workspace/landing/dados"

collections = {
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

# COMMAND ----------

dbutils.fs.mkdirs(caminho_landing)

for arquivo in dbutils.fs.ls(caminho_landing):
    if arquivo.name.endswith(".json"):
        dbutils.fs.rm(arquivo.path)

# COMMAND ----------

client = MongoClient(
    mongodb_uri,
    tls=True,
    tlsCAFile=certifi.where(),
    serverSelectionTimeoutMS=20000,
)
database = client[mongodb_database]

for collection_name, source_column in collections.items():
    docs = database[collection_name].find({}, {"_id": 0}).sort("id_linha", 1)
    output_path = Path(caminho_landing) / f"{collection_name}.json"

    with output_path.open("w", encoding="utf-8") as output:
        for doc in docs:
            value = doc.get("valor", doc.get(source_column))
            json.dump(
                {
                    "id_linha": doc.get("id_linha"),
                    source_column: value,
                    "collection_origem": collection_name,
                },
                output,
                ensure_ascii=False,
            )
            output.write("\n")

client.close()

# COMMAND ----------

display(dbutils.fs.ls(caminho_landing))
