from __future__ import annotations

import json
import sys
from pathlib import Path
from urllib.parse import urlparse

from pymongo import MongoClient
from pymongo.errors import ConfigurationError, OperationFailure, ServerSelectionTimeoutError


ROOT = Path(__file__).resolve().parents[1]
COLLECTIONS_DIR = ROOT / "data" / "mongodb" / "collections"
DEFAULT_DATABASE = "ai_job_market"


def database_from_uri(uri: str) -> str:
    path = urlparse(uri).path.strip("/")
    return path or DEFAULT_DATABASE


def main() -> int:
    if len(sys.argv) != 2:
        print(
            "Uso: python scripts/import_mongodb_collections.py "
            "\"mongodb+srv://usuario:SENHA@cluster.mongodb.net/ai_job_market?appName=databricks\""
        )
        return 1

    uri = sys.argv[1]
    database_name = database_from_uri(uri)

    try:
        client = MongoClient(uri, serverSelectionTimeoutMS=10000)
        client.admin.command("ping")
    except ConfigurationError as error:
        print("Erro na URI do MongoDB Atlas.")
        print("Verifique se usuario e senha estao corretos e se caracteres especiais foram codificados.")
        print("Exemplo: @ vira %40, # vira %23, & vira %26.")
        print(f"Detalhe tecnico: {error}")
        return 1
    except OperationFailure as error:
        print("Falha de autenticacao no MongoDB Atlas.")
        print("Verifique usuario, senha e permissoes em Database Access.")
        print(f"Detalhe tecnico: {error}")
        return 1
    except ServerSelectionTimeoutError as error:
        print("Nao foi possivel conectar ao cluster do MongoDB Atlas.")
        print("Verifique se o cluster esta ativo e se seu IP foi liberado em Network Access.")
        print("No Atlas, use Add Current IP Address ou libere temporariamente 0.0.0.0/0 apenas para teste.")
        print(f"Detalhe tecnico: {error}")
        return 1

    database = client[database_name]

    files = sorted(COLLECTIONS_DIR.glob("*.json"))
    if not files:
        print(f"Nenhum JSON encontrado em {COLLECTIONS_DIR}")
        return 1

    for file_path in files:
        collection_name = file_path.stem
        with file_path.open("r", encoding="utf-8-sig") as file:
            documents = json.load(file)

        if not isinstance(documents, list):
            raise ValueError(f"O arquivo {file_path} precisa conter um JSON Array.")

        try:
            collection = database[collection_name]
            collection.delete_many({})

            if documents:
                collection.insert_many(documents)

            print(f"{collection_name}: {len(documents)} documentos importados")
        except OperationFailure as error:
            print(f"Erro ao importar a collection '{collection_name}'.")
            print("Verifique se o usuario possui permissao de leitura e escrita no database.")
            print(f"Detalhe tecnico: {error}")
            return 1

    client.close()
    print(f"Importacao finalizada no database '{database_name}'.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
