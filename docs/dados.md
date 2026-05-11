# Base de Dados

A fonte não relacional utilizada no projeto e o MongoDB Atlas.

O banco `ai_job_market` foi planejado a partir do arquivo original `ai_job_market_insights.csv`, armazenado em `data/raw/`.

## Fonte Original

| Arquivo | Registros | Colunas |
| --- | ---: | ---: |
| `ai_job_market_insights.csv` | 500 | 10 |

## Collections no MongoDB Atlas

Cada coluna do arquivo original foi preparada como uma collection separada. Os arquivos para importar no Atlas estao em `data/mongodb/collections/`.

Cada documento possui:

- `id_linha`: identificador da linha original;
- `valor`: valor da coluna;
- `coluna_origem`: nome da coluna original.

| Collection | Registros | Coluna original |
| --- | ---: | --- |
| `job_title` | 500 | `Job_Title` |
| `industry` | 500 | `Industry` |
| `company_size` | 500 | `Company_Size` |
| `location` | 500 | `Location` |
| `ai_adoption_level` | 500 | `AI_Adoption_Level` |
| `automation_risk` | 500 | `Automation_Risk` |
| `required_skills` | 500 | `Required_Skills` |
| `salary_usd` | 500 | `Salary_USD` |
| `remote_friendly` | 500 | `Remote_Friendly` |
| `job_growth_projection` | 500 | `Job_Growth_Projection` |

## Extracao Para Landing

O notebook `002 - Extracao` conecta no MongoDB Atlas, le todas as collections e grava um JSON por collection no volume:

```text
/Volumes/workspace/landing/dados/
```

## Relacionamento Entre Collections

Todas as collections se relacionam pelo campo `id_linha`.

```text
job_title.id_linha
industry.id_linha
company_size.id_linha
location.id_linha
ai_adoption_level.id_linha
automation_risk.id_linha
required_skills.id_linha
salary_usd.id_linha
remote_friendly.id_linha
job_growth_projection.id_linha
```

Esse desenho permite extrair dados de uma fonte não relacional e reconstruir a linha completa na camada Silver.

