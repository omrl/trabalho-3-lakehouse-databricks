# 002 - Extracao

Este notebook representa a primeira etapa do trabalho: extrair todas as collections de um banco não relacional e gravar arquivos JSON na Landing.

## Entrada

MongoDB Atlas:

```text
Database: ai_job_market
```

## Saida

Arquivos JSON no volume:

```text
/Volumes/workspace/landing/dados/
```

## Responsabilidades

- Conectar ao MongoDB Atlas.
- Ler as collections da fonte.
- Extrair todos os documentos de cada collection.
- Gerar um JSON para cada collection no volume da Landing.
- Manter o campo `id_linha` para permitir a reconstrucao da base na Silver.

## Tabelas Extraidas

- `job_title`
- `industry`
- `company_size`
- `location`
- `ai_adoption_level`
- `automation_risk`
- `required_skills`
- `salary_usd`
- `remote_friendly`
- `job_growth_projection`

## Papel no Pipeline

A extracao separa a fonte MongoDB Atlas da camada Lakehouse. Depois dela, a Bronze passa a consumir apenas os arquivos JSON da Landing.

