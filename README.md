# dashboard-analise-reserva-petroleo

# 🌍 Dashboard de Análise das Reservas Mundiais de Petróleo

Este projeto consiste em um dashboard interativo desenvolvido em **Python** com **Streamlit**, **Pandas** e **Plotly**, com o objetivo de analisar e visualizar dados sobre as reservas mundiais de petróleo.

A análise é realizada **para um único ano por vez**, permitindo visualizar o total de reservas registrado naquele período. Ao selecionar um ano diferente, todos os indicadores e gráficos são atualizados com os valores correspondentes àquele ano, possibilitando comparar a evolução das reservas ao longo do tempo e identificar se houve aumento ou redução em relação aos anos anteriores.

## 📌 Funcionalidades

* Filtragem por ano
* Filtragem por tipo de bloco
* Filtragem por região geográfica
* Filtragem por país
* Exibição de indicadores (KPIs)
* Gráficos interativos
* Mapa mundial das reservas de petróleo

## 🧹 Pré-processamento dos Dados

Antes da construção do dashboard, foi realizado o pré-processamento da base de dados, juntamente com uma **Análise Exploratória dos Dados (EDA)**, para garantir a qualidade e a confiabilidade das informações utilizadas.

As principais etapas incluíram:

* Limpeza e organização dos dados
* Tratamento de inconsistências
* Padronização das informações
* Análise exploratória para identificar padrões e compreender a estrutura dos dados
* Preparação da base para a geração dos indicadores e visualizações

## 📊 Indicadores (KPIs)

O dashboard apresenta informações como:

* Quantidade total de reservas de petróleo no ano selecionado
* Maior reserva registrada entre os países no ano selecionado
* Região com maior número de países produtores
* País com a maior reserva de petróleo no ano selecionado

## 🛠️ Tecnologias Utilizadas

* Python
* Streamlit
* Pandas
* Plotly Express

## ▶️ Como executar

1. Clone este repositório:

```bash
git clone https://github.com/seu-usuario/dashboard-petroleo.git
```

2. Instale as dependências:

```bash
pip install -r requirements.txt
```

3. Execute a aplicação:

```bash
streamlit run app.py
```

## 📂 Base de Dados

O conjunto de dados contém informações anuais sobre as reservas mundiais de petróleo, incluindo:

* País
* Região Geográfica
* Ano
* Tipo de Bloco
* Reserva de Petróleo
* Código ISO3

## 🎯 Objetivo

Este projeto foi desenvolvido para aplicar conhecimentos em **Análise Exploratória de Dados (EDA)**, **pré-processamento**, **visualização de dados** e **desenvolvimento de dashboards interativos**, permitindo explorar e comparar a evolução das reservas mundiais de petróleo ao longo dos anos.

---

**Desenvolvido por Matheus Silva**
**
