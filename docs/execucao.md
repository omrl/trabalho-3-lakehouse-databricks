# Execucao

Esta pagina descreve como executar o projeto no Databricks Free Edition.

## Pre-requisitos

- Conta no Databricks Free Edition.
- Permissao para criar schemas, volumes e tabelas no workspace.
- Banco `ai_job_market` criado no MongoDB Atlas.
- Collections importadas a partir dos arquivos de `data/mongodb/collections/`.
- Notebooks `.ipynb` disponiveis na pasta `notebooks/`.

## Importacao dos Notebooks

No Databricks:

1. Acesse `Workspace`.
2. Escolha a pasta onde deseja importar os notebooks.
3. Clique em `Import`.
4. Selecione os arquivos `.ipynb` da pasta `notebooks/`.
5. Confirme a importacao como notebooks.

## Preparacao do MongoDB Atlas

No MongoDB Atlas:

1. Crie um cluster gratuito.
2. Crie o banco `ai_job_market`.
3. Importe os arquivos de `data/mongodb/collections/`.
4. Use o nome do arquivo como nome da collection.
5. Copie a connection string do Atlas.

Depois, o notebook `002 - Extracao` gera os JSONs no volume:

```text
/Volumes/workspace/landing/dados/
```

## Ordem de Execucao

Execute os notebooks nesta ordem:

| Ordem | Notebook | Objetivo |
| ---: | --- | --- |
| 1 | `001 - Preparando ambiente` | Cria schemas e volumes |
| 2 | `002 - Extracao` | Extrai collections do MongoDB Atlas para JSON na Landing |
| 3 | `003 - Bronze` | Carrega JSONs como tabelas Delta Bronze |
| 4 | `004 - Silver` | Trata, qualifica e remonta a base pelo `id_linha` |
| 5 | `005 - Gold` | Cria dimensoes e fato para analise do mercado de IA |

O notebook `006 - Destruindo ambiente` nao faz parte da execucao principal. Ele serve para limpar o ambiente em caso de reprocessamento completo.

## Validacoes

Apos executar o fluxo, valide:

- se as collections existem no MongoDB Atlas;
- se os JSONs foram gerados no volume `workspace.landing.dados`;
- se as tabelas foram criadas no schema `bronze`;
- se as tabelas tratadas foram criadas no schema `silver`;
- se as dimensoes e a fato foram criadas no schema `gold`;
- se a Job terminou com status de sucesso.

## Executando a Documentacao MkDocs

Para visualizar a documentacao localmente:

```bash
pip install -r requirements.txt
mkdocs serve
```

Depois acesse:

```text
http://127.0.0.1:8000
```

Para gerar a versao estatica:

```bash
mkdocs build
```

