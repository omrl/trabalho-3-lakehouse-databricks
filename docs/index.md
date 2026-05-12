# Lakehouse com Databricks Free Edition

Este projeto implementa um pipeline Lakehouse no Databricks Free Edition usando a Arquitetura Medalhao.

O trabalho utiliza um banco não relacional no MongoDB Atlas criado a partir da base `ai_job_market_insights.csv`. O pipeline extrai todas as collections desse banco para JSON na Landing e processa os dados nas camadas `Bronze`, `Silver` e `Gold`.

## Objetivo

O objetivo principal e demonstrar um fluxo completo de Engenharia de Dados:

- recepcao dos arquivos brutos;
- extracao de collections de um banco não relacional;
- persistencia dos dados em Delta Lake;
- tratamento e aplicacao de Data Quality;
- criacao de tabelas analiticas;
- execucao orquestrada por Job no Databricks.

## Fluxo Geral

```text
MongoDB Atlas -> JSON/Landing -> Bronze -> Silver -> Gold
```

Cada etapa foi implementada em um notebook separado, permitindo que o pipeline seja executado de forma modular ou encadeado em uma Job.

## Entregaveis

- Arquivos JSON para carga no MongoDB Atlas em `data/mongodb/collections/`.
- Arquivos JSON extraidos para a Landing.
- Notebooks em formato `.ipynb` na pasta `notebooks/`.
- Documentacao em MkDocs na pasta `docs/`.
- Arquivo `mkdocs.yml` para gerar a documentacao.
- `README.md` explicando o projeto no GitHub.

## Schemas Criados

| Schema | Papel |
| --- | --- |
| `workspace.landing` | Entrada dos arquivos brutos |
| `workspace.bronze` | Dados em Delta Lake com estrutura da origem |
| `workspace.silver` | Dados tratados e qualificados |
| `workspace.gold` | Modelo dimensional para analise |

## Como Ler Esta Documentacao

Comece pela pagina de arquitetura para entender a divisao das camadas. Depois consulte a base de dados, os notebooks e a configuracao da Job no Databricks.
