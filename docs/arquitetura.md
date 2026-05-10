# Arquitetura

O projeto segue a Arquitetura Medalhao, uma abordagem comum em Lakehouse para organizar dados por nivel de refinamento.

## Visao Geral

```mermaid
%%{init: {"theme": "base", "themeVariables": {"primaryTextColor": "#ffffff", "tertiaryTextColor": "#ffffff", "nodeTextColor": "#ffffff", "fontFamily": "Arial"}}}%%
flowchart LR
    csv[(Arquivos CSV<br/>Base relacional de seguros)]
    landing[(Landing<br/>Volume dados<br/>Arquivos brutos)]
    bronze[(Bronze<br/>Delta Lake<br/>Estrutura da origem)]
    silver[(Silver<br/>Delta Lake<br/>Dados qualificados)]
    gold[(Gold<br/>Modelo dimensional<br/>Analise de negocio)]
    job[Databricks Job<br/>Orquestracao dos notebooks]

    csv -->|Ingestao| landing
    landing -->|Notebook 002| bronze
    bronze -->|Notebook 003<br/>Data Quality| silver
    silver -->|Notebook 004<br/>Dimensoes e fatos| gold

    job -.-> landing
    job -.-> bronze
    job -.-> silver
    job -.-> gold

    classDef source fill:#1f2937,stroke:#9ca3af,color:#ffffff
    classDef layer fill:#0f766e,stroke:#99f6e4,color:#ffffff
    classDef process fill:#f97316,stroke:#fed7aa,color:#ffffff
    linkStyle default stroke:#475569,color:#111827

    class csv source
    class landing,bronze,silver,gold layer
    class job process

    style csv color:#ffffff
    style landing color:#ffffff
    style bronze color:#ffffff
    style silver color:#ffffff
    style gold color:#ffffff
    style job color:#ffffff
```

## Landing

A Landing e a camada de entrada. Nela ficam os arquivos CSV exatamente como recebidos.

No Databricks, essa camada foi representada pelo schema `workspace.landing` e pelo volume `workspace.landing.dados`.

Responsabilidades:

- armazenar os arquivos brutos;
- preservar a origem dos dados;
- servir como ponto inicial de reprocessamento.

## Bronze

A Bronze transforma os arquivos CSV em tabelas Delta.

Responsabilidades:

- ler os arquivos da Landing;
- criar tabelas Delta;
- manter a granularidade original;
- adicionar metadados de processamento quando necessario.

Essa camada ainda esta proxima da fonte, com pouca regra de negocio aplicada.

## Silver

A Silver e a camada de dados tratados.

Responsabilidades:

- padronizar nomes e formatos;
- corrigir tipos de dados;
- remover ou tratar inconsistencias;
- aplicar regras de qualidade;
- preparar dados para modelagem dimensional.

## Gold

A Gold e a camada de consumo analitico.

Responsabilidades:

- disponibilizar dimensoes;
- disponibilizar tabela fato;
- reduzir complexidade para consultas;
- apoiar analises de apolices, clientes, veiculos e sinistros.

O desenho segue a abordagem dimensional de Ralph Kimball, separando entidades descritivas em dimensoes e eventos/medidas em fatos.
