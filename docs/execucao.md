# Execucao

Esta pagina descreve como executar o projeto no Databricks Free Edition.

## Pre-requisitos

- Conta no Databricks Free Edition.
- Permissao para criar schemas, volumes e tabelas no workspace.
- Arquivos CSV disponiveis na pasta `data/csv/`.
- Notebooks `.dbc` disponiveis na pasta `notebooks/dbc/`.

## Importacao dos Notebooks

No Databricks:

1. Acesse `Workspace`.
2. Escolha a pasta onde deseja importar os notebooks.
3. Clique em `Import`.
4. Selecione os arquivos `.dbc` da pasta `notebooks/dbc/`.
5. Confirme a importacao.

## Upload dos CSVs

Os CSVs devem ser enviados para o volume da camada Landing:

```text
workspace.landing.dados
```

O caminho fisico esperado no Databricks segue o formato:

```text
/Volumes/workspace/landing/dados/
```

## Ordem de Execucao

Execute os notebooks nesta ordem:

| Ordem | Notebook | Objetivo |
| ---: | --- | --- |
| 1 | `001 - Preparando ambiente` | Cria schemas e volume |
| 2 | `002 - Bronze` | Carrega CSVs como tabelas Delta Bronze |
| 3 | `003 - Silver` | Trata e qualifica os dados |
| 4 | `004 - Gold` | Cria modelo dimensional |

O notebook `005 - Destruindo ambiente` nao faz parte da execucao principal. Ele serve para limpar o ambiente em caso de reprocessamento completo.

## Validacoes

Apos executar o fluxo, valide:

- se os arquivos estao no volume da Landing;
- se as tabelas foram criadas no schema `bronze`;
- se as tabelas tratadas foram criadas no schema `silver`;
- se as dimensoes e a fato foram criadas no schema `gold`;
- se a Job terminou com status de sucesso.

## Executando a Documentacao MkDocs

Para visualizar a documentacao localmente:

```bash
pip install -r requirements.txt
mkdocs serve
```

Depois acesse:

```text
http://127.0.0.1:8000
```

Para gerar a versao estatica:

```bash
mkdocs build
```
