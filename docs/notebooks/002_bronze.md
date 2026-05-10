# 002 - Bronze

Este notebook le os arquivos CSV armazenados na Landing e cria tabelas Delta na camada Bronze.

## Entrada

Arquivos CSV no volume:

```text
/Volumes/workspace/landing/dados/
```

## Saida

Tabelas Delta no schema:

```text
workspace.bronze
```

## Responsabilidades

- Ler os arquivos CSV.
- Identificar cabecalho e separador.
- Converter os dados para DataFrames Spark.
- Gravar as tabelas em formato Delta Lake.
- Preservar a estrutura da origem.

## Tabelas Processadas

- `apolice`
- `carro`
- `cliente`
- `endereco`
- `estado`
- `marca`
- `modelo`
- `municipio`
- `regiao`
- `sinistro`
- `telefone`

## Papel no Pipeline

A Bronze e a primeira camada estruturada do Lakehouse. Ela permite rastrear os dados conforme chegaram da origem e serve como base para a camada Silver.
