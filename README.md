# 🚀 Data Engineering Project - E-commerce

## 📌 Visão geral
Pipeline de dados completo simulando um ambiente de produção, utilizando arquitetura medalhão (Bronze, Silver e Gold) para transformar dados brutos em dados analíticos prontos para consumo em BI.

## 🧱 Arquitetura

- **Bronze**: ingestão de dados brutos (CSV → Parquet)
- **Silver**: limpeza, tratamento e enriquecimento (joins entre tabelas)
- **Gold**: criação de métricas de negócio (KPIs)

## 🔄 Pipeline de dados

1. Extração de dados de múltiplas fontes (dataset de e-commerce)
2. Armazenamento em Data Lake (simulado localmente)
3. Transformações com Python (Pandas)
4. Modelagem analítica (dataset final)
5. Disponibilização para consumo em ferramentas de BI

## ⚙️ Tecnologias utilizadas

- Python
- Pandas
- Parquet
- Arquitetura ELT
- Modelagem dimensional

## 📊 Dataset final (Gold Layer)

Tabela analítica contendo:

- Receita diária
- Quantidade de pedidos
- Ticket médio

## 📁 Estrutura do projeto

data-engineer-project/
│
├── data/
│   ├── raw/
│   ├── bronze/
│   ├── silver/
│   └── gold/
│
└── pipelines/
    ├── bronze.py
    ├── silver.py
    └── gold.py

## ⚠️ Boas práticas aplicadas

- Separação em camadas (arquitetura medalhão)
- Uso de formato columnar (Parquet)
- Dados não versionados no repositório
- Pipeline reprodutível

## 🚀 Próximos passos

- Orquestração com Airflow
- Processamento distribuído com Spark
- Deploy em cloud (Azure / AWS)