# Job no Databricks

Os notebooks foram encadeados em uma Job no Databricks para garantir a execucao sequencial do pipeline.

## Objetivo da Job

A Job automatiza o fluxo completo:

```text
Preparar ambiente -> Extracao -> Bronze -> Silver -> Gold
```

Com isso, a execucao deixa de depender de rodar manualmente cada notebook em separado.

## Tarefas da Job

| Ordem | Tarefa | Dependencia |
| ---: | --- | --- |
| 1 | `001 - Preparando ambiente` | Nenhuma |
| 2 | `002 - Extracao` | Executa apos o ambiente estar pronto e extrai do MongoDB Atlas |
| 3 | `003 - Bronze` | Executa apos a extracao |
| 4 | `004 - Silver` | Executa apos a Bronze |
| 5 | `005 - Gold` | Executa apos a Silver |

## Fluxo de Dependencias

```text
001 Preparando ambiente
        │
        ▼
000 Extracao
        │
        ▼
002 Bronze
        │
        ▼
003 Silver
        │
        ▼
004 Gold
```

## Resultado Esperado

Ao final da Job, o ambiente deve conter:

- schema `workspace.landing` com volume de dados;
- schema `workspace.bronze` com tabelas Delta da origem;
- schema `workspace.silver` com dados tratados;
- schema `workspace.gold` com tabelas dimensionais e tabela fato.

## Observacao

O notebook de destruicao do ambiente deve ficar fora da Job principal. Ele deve ser executado apenas quando for necessario apagar os objetos criados e reiniciar o processo.

