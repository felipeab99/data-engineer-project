# 🚀 Data Engineering Project - E-commerce

## 📌 Visão geral
Pipeline de dados completo simulando um ambiente de produção, utilizando arquitetura medalhão (Bronze, Silver e Gold) para transformar dados brutos em informações analíticas.

## 🧱 Arquitetura

- **Bronze**: ingestão de dados brutos (CSV → Parquet)
- **Silver**: limpeza, tratamento e enriquecimento (joins)
- **Gold**: criação de métricas de negócio (KPIs)

## 🔄 Pipeline de dados

1. Extração de dados (dataset público de e-commerce)
2. Armazenamento em Data Lake (local)
3. Transformações com Python (Pandas)
4. Modelagem analítica
5. Geração de dataset final para BI

## ⚙️ Tecnologias utilizadas

- Python
- Pandas
- Parquet
- Arquitetura ELT
- Modelagem de dados

## 📊 Dataset final (Gold Layer)

Tabela com métricas de negócio:

- Receita diária
- Quantidade de pedidos
- Ticket médio

## 📁 Estrutura do projeto
data-engineer-project/
│
├── data/ # Data Lake (não versionado)
│ ├── raw/
│ ├── bronze/
│ ├── silver/
│ └── gold/
│
├── pipelines/ # Scripts de processamento
│ ├── bronze.py
│ ├── silver.py
│ └── gold.py

## ⚠️ Boas práticas aplicadas

- Separação em camadas (arquitetura medalhão)
- Uso de formato columnar (Parquet)
- Dados não versionados no repositório
- Pipeline reprodutível

## 🚀 Próximos passos

- Orquestração com Airflow
- Processamento distribuído com Spark
- Deploy em cloud (Azure / AWS)