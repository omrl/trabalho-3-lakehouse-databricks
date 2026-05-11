# 003 - Bronze

Este notebook le os arquivos JSON armazenados na Landing e cria tabelas Delta na camada Bronze.

## Entrada

Arquivos JSON no volume:

```text
/Volumes/workspace/landing/dados/
```

## Saida

Tabelas Delta no schema:

```text
workspace.bronze
```

## Responsabilidades

- Ler os arquivos JSON.
- Converter os dados para DataFrames Spark.
- Gravar as tabelas em formato Delta Lake.
- Preservar a estrutura da origem.

## Tabelas Processadas

- `ai_adoption_level`
- `automation_risk`
- `company_size`
- `industry`
- `job_growth_projection`
- `job_title`
- `location`
- `remote_friendly`
- `required_skills`
- `salary_usd`

## Papel no Pipeline

A Bronze e a primeira camada estruturada do Lakehouse. Ela permite rastrear os dados conforme chegaram da origem e serve como base para a camada Silver.

