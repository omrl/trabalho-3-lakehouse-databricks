# 004 - Silver

Este notebook le as tabelas Bronze e cria tabelas tratadas na camada Silver.

## Entrada

Tabelas Delta no schema:

```text
workspace.bronze
```

## Saida

Tabelas Delta no schema:

```text
workspace.silver
```

## Responsabilidades

- Ajustar tipos de dados.
- Padronizar textos.
- Tratar espacos em campos textuais.
- Validar chaves e campos obrigatorios.
- Remover ou tratar registros inconsistentes.
- Reunir os arquivos separados por coluna usando `id_linha`.
- Preparar os dados para a modelagem dimensional.

## Data Quality

A camada Silver concentra as regras de qualidade do pipeline. Exemplos de verificacoes aplicaveis:

- campos identificadores nao nulos;
- `id_linha` valido e nao nulo;
- valores monetarios numericos;
- textos sem espacos excedentes;
- relacionamentos coerentes entre tabelas.

## Papel no Pipeline

A Silver reduz problemas vindos da origem e fornece uma base confiavel para criacao das dimensoes e fatos na Gold.

