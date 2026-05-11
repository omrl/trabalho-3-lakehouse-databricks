# Modelo Gold

A camada Gold foi planejada com foco analitico, seguindo os principios da modelagem dimensional de Ralph Kimball.

## Objetivo

Transformar os dados tratados da Silver em tabelas de facil consumo para analises sobre o mercado de trabalho em inteligencia artificial.

Exemplos de perguntas que a Gold pode responder:

- Quais cargos possuem maior media salarial?
- Quais setores concentram mais oportunidades?
- Como o risco de automacao varia por cargo ou industria?
- Quais habilidades aparecem com maior frequencia?
- Quais localidades possuem mais oportunidades remotas?
- Como a projecao de crescimento se distribui por cargo, setor e porte da empresa?

## Dimensoes

As dimensoes armazenam atributos descritivos da base.

### `gold.dim_cargo`

Representa os cargos analisados.

Campos esperados:

- chave substituta do cargo;
- titulo do cargo;
- habilidade exigida;
- risco de automacao;
- projecao de crescimento.

### `gold.dim_empresa`

Representa o contexto empresarial da oportunidade.

Campos esperados:

- chave substituta da empresa;
- industria;
- porte da empresa;
- nivel de adocao de IA.

### `gold.dim_localidade`

Representa a localizacao da oportunidade.

Campos esperados:

- chave substituta da localidade;
- localizacao;
- indicador de trabalho remoto.

## Fato

### `gold.fato_mercado_ia`

Tabela voltada para analise das oportunidades do mercado de IA.

Possiveis medidas:

- salario em dolares;
- quantidade de registros;
- quantidade de oportunidades por cargo;
- quantidade de oportunidades por industria;
- quantidade de oportunidades remotas.

Possiveis chaves:

- cargo;
- empresa;
- localidade.

## Granularidade

A granularidade recomendada para a fato e uma linha por registro original da base `ai_job_market_insights.csv`, preservando o campo `id_linha` como referencia tecnica.

## Beneficio da Modelagem

Separar dimensoes e fatos facilita consultas analiticas, reduz repeticao de atributos e aproxima a camada Gold de um modelo preparado para BI, dashboards e indicadores.
