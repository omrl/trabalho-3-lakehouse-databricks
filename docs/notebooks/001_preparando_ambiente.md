# 001 - Preparando Ambiente

Este notebook cria os objetos basicos usados pelo projeto no Databricks.

## Responsabilidades

- Criar o schema `workspace.landing`.
- Criar o volume `workspace.landing.dados`.
- Criar o schema `workspace.bronze`.
- Criar o schema `workspace.silver`.
- Criar o schema `workspace.gold`.

## Papel no Pipeline

Ele deve ser executado antes dos demais notebooks, pois as etapas seguintes dependem dos schemas e do volume da Landing.

## Objetos Criados

```sql
CREATE SCHEMA IF NOT EXISTS workspace.landing;
CREATE VOLUME IF NOT EXISTS workspace.landing.dados;
CREATE SCHEMA IF NOT EXISTS workspace.bronze;
CREATE SCHEMA IF NOT EXISTS workspace.silver;
CREATE SCHEMA IF NOT EXISTS workspace.gold;
```

## Observacao

Caso o ambiente ja exista, os comandos com `IF NOT EXISTS` evitam erro por recriacao dos objetos.
