# 004 - Gold

Este notebook cria a camada analitica do projeto.

## Entrada

Tabelas tratadas no schema:

```text
workspace.silver
```

## Saida

Tabelas dimensionais no schema:

```text
workspace.gold
```

## Responsabilidades

- Criar dimensoes.
- Criar tabela fato.
- Gerar chaves substitutas quando necessario.
- Realizar joins entre tabelas Silver.
- Disponibilizar dados organizados para analise.

## Modelo Dimensional

A camada Gold segue a abordagem de Ralph Kimball:

- dimensoes guardam atributos descritivos;
- fatos guardam eventos e medidas;
- chaves substitutas simplificam os relacionamentos analiticos.

## Exemplos de Tabelas

- `gold.dim_cliente`
- `gold.dim_carro`
- `gold.dim_localidade`
- `gold.fato_apolice_sinistro`

## Papel no Pipeline

A Gold e a camada final do Lakehouse e representa a area de consumo para consultas SQL, dashboards e indicadores.
