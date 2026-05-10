# Modelo Gold

A camada Gold foi construida com foco analitico, seguindo a modelagem dimensional proposta por Ralph Kimball.

## Objetivo

Transformar os dados tratados da Silver em tabelas de facil consumo para analises de negocio.

Exemplos de perguntas que a Gold pode responder:

- Quantas apolices existem por periodo?
- Qual o valor total de cobertura por cliente?
- Quais marcas e modelos possuem mais sinistros?
- Como os sinistros se distribuem por municipio, estado ou regiao?
- Qual o perfil dos clientes segurados?

## Dimensoes

As dimensoes armazenam atributos descritivos do negocio.

### `gold.dim_cliente`

Representa os clientes segurados.

Campos esperados:

- chave substituta do cliente;
- codigo original do cliente;
- nome;
- CPF;
- sexo;
- data de nascimento;
- telefone;
- endereco.

### `gold.dim_carro`

Representa os veiculos segurados.

Campos esperados:

- chave substituta do carro;
- placa;
- marca;
- modelo;
- cor;
- ano;
- chassi.

### `gold.dim_localidade`

Representa a localizacao geografica.

Campos esperados:

- chave substituta da localidade;
- codigo do municipio;
- municipio;
- estado;
- regiao.

### `gold.dim_tempo`

Quando utilizada, representa datas relevantes para analise, como inicio e fim de vigencia da apolice ou data de sinistro.

Campos esperados:

- data;
- ano;
- mes;
- dia;
- trimestre;
- nome do mes.

## Fato

A tabela fato concentra eventos e medidas.

### `gold.fato_apolice_sinistro`

Tabela voltada para analise de apolices e sinistros.

Possiveis medidas:

- valor de cobertura;
- valor de franquia;
- quantidade de apolices;
- quantidade de sinistros.

Possiveis chaves:

- cliente;
- carro;
- localidade;
- data de inicio da vigencia;
- data de fim da vigencia;
- data do sinistro.

## Granularidade

A granularidade recomendada para a fato e uma linha por apolice e sinistro associado, preservando tambem apolices sem sinistro quando a regra de negocio exigir analise de contratos ativos.

## Beneficio da Modelagem

Separar dimensoes e fatos reduz a complexidade das consultas e melhora a organizacao da camada analitica. A Gold fica mais proxima de um modelo de BI, facilitando consultas SQL, dashboards e indicadores.
