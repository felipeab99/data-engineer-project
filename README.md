# 🏗️ Data Engineering Pipeline — Olist E-commerce

Pipeline de engenharia de dados end-to-end usando dados públicos do e-commerce brasileiro Olist.

## 📐 Arquitetura 

CSV (Kaggle/Olist)
↓
[Bronze]  → Conversão CSV → Parquet
↓
[Silver]  → Limpeza e junção das tabelas
↓
[Gold]   → Métricas agregadas de vendas
↓
Databricks → Análise exploratória com PySpark

Todas as camadas armazenadas no **Azure Data Lake Gen2**.
Pipeline orquestrado pelo **Apache Airflow**.

## 🛠️ Stack

| Ferramenta | Uso |
|---|---|
| Python | Transformações dos dados |
| Apache Airflow | Orquestração do pipeline |
| Docker | Containerização do Airflow |
| Azure Data Lake Gen2 | Armazenamento Bronze/Silver/Gold |
| PySpark | Análise exploratória dos dados |
| Databricks | Ambiente de processamento distribuído |

## 📊 Camadas

**Bronze** — Ingestão raw: converte os CSVs do Olist para Parquet sem transformações.

**Silver** — Limpeza e enriquecimento: filtra pedidos entregues, faz joins entre orders, items, customers, products e payments.

**Gold** — Agregação: métricas diárias de receita, pedidos e ticket médio.

## 🔍 Análises (PySpark)

- Receita total: R$ 13,8 milhões
- Maior dia de vendas: 24/11/2017 (Black Friday) — R$ 152k
- Crescimento consistente de 2016 a 2018

## 📁 Estrutura
├── dags/
│   └── pipeline_dag.py
├── pipelines/
│   ├── bronze.py
│   ├── silver.py
│   ├── gold.py
│   └── azure_client.py
├── data/
│   └── raw/
└── docker-compose.yml

## 🚀 Como rodar

```bash
# 1. Clone o repositório
git clone https://github.com/felipeab99/data-engineer-project

# 2. Configure o .env com sua Azure Connection String
AZURE_CONNECTION_STRING=sua_connection_string

# 3. Suba o Airflow
cd airflow
docker-compose up -d

# 4. Acesse localhost:8080 e rode o DAG olist_pipeline
```

## 📦 Dataset

[Olist E-commerce Dataset — Kaggle](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce)
