# Base de Dados

A base utilizada representa um cenario de seguros de automoveis. Os arquivos estao no diretorio `data/csv/`.

## Arquivos

| Arquivo | Registros | Campos |
| --- | ---: | --- |
| `apolice.csv` | 10.000 | `cd_apolice`, `cd_cliente`, `dt_inicio_vigencia`, `dt_fim_vigencia`, `vl_cobertura`, `vl_franquia`, `placa` |
| `carro.csv` | 10.002 | `placa`, `cd_modelo`, `chassi`, `ano`, `cor` |
| `cliente.csv` | 20.010 | `cd_cliente`, `nome`, `cpf`, `sexo`, `dt_nascimento` |
| `endereco.csv` | 20.010 | `cd_cliente`, `cd_municipio`, `ds_endereco`, `nr_endereco`, `bairro` |
| `estado.csv` | 27 | `cd_estado`, `cd_regiao`, `nm_estado`, `sigla_uf` |
| `marca.csv` | 10 | `cd_marca`, `nm_marca` |
| `modelo.csv` | 100 | `cd_modelo`, `cd_marca`, `nm_modelo` |
| `municipio.csv` | 5.570 | `cd_municipio`, `nm_municipio`, `cd_estado` |
| `regiao.csv` | 5 | `cd_regiao`, `nm_regiao` |
| `sinistro.csv` | 10.000 | `cd_sinistro`, `placa`, `dt_sinistro`, `local_sinistro`, `condutor` |
| `telefone.csv` | 20.010 | `cd_cliente`, `nr_telefone` |

## Entidades Principais

### Cliente

Representa os segurados. Possui dados cadastrais como nome, CPF, sexo e data de nascimento.

### Apolice

Representa os contratos de seguro, com periodo de vigencia, valor de cobertura, franquia, cliente e veiculo associado.

### Carro

Representa os veiculos segurados, com placa, modelo, chassi, ano e cor.

### Sinistro

Representa ocorrencias relacionadas aos veiculos, contendo data, local e condutor.

### Localidade

E composta por municipio, estado e regiao. Essa estrutura permite analises por distribuicao geografica.

## Relacionamentos Esperados

```text
cliente 1 ── N apolice
cliente 1 ── N telefone
cliente 1 ── N endereco
apolice N ── 1 carro
carro N ── 1 modelo
modelo N ── 1 marca
sinistro N ── 1 carro
endereco N ── 1 municipio
municipio N ── 1 estado
estado N ── 1 regiao
```

Esses relacionamentos servem como base para a construcao das tabelas dimensionais na camada Gold.
