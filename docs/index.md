# Lakehouse com Databricks Free Edition

Este projeto implementa um pipeline Lakehouse no Databricks Free Edition usando a Arquitetura Medalhao.

O trabalho utiliza arquivos CSV de uma base relacional de seguros e organiza o processamento nas camadas `Landing`, `Bronze`, `Silver` e `Gold`.

## Objetivo

O objetivo principal e demonstrar um fluxo completo de Engenharia de Dados:

- recepcao dos arquivos brutos;
- persistencia dos dados em Delta Lake;
- tratamento e aplicacao de Data Quality;
- criacao de tabelas analiticas;
- execucao orquestrada por Job no Databricks.

## Fluxo Geral

```text
CSV -> Landing -> Bronze -> Silver -> Gold
```

Cada etapa foi implementada em um notebook separado, permitindo que o pipeline seja executado de forma modular ou encadeado em uma Job.

## Entregaveis

- Arquivos CSV da base em `data/csv/`.
- Notebooks exportados em `.dbc` em `notebooks/dbc/`.
- Versao extraida dos notebooks em scripts `.py` legiveis em `notebooks/python/`.
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
