import pandas as pd
import os

BRONZE_PATH = "data/bronze/"
SILVER_PATH = "data/silver/"

os.makedirs(SILVER_PATH, exist_ok=True)

# 📥 carregar dados
orders = pd.read_parquet(BRONZE_PATH + "olist_orders_dataset.parquet")
items = pd.read_parquet(BRONZE_PATH + "olist_order_items_dataset.parquet")
customers = pd.read_parquet(BRONZE_PATH + "olist_customers_dataset.parquet")
products = pd.read_parquet(BRONZE_PATH + "olist_products_dataset.parquet")
payments = pd.read_parquet(BRONZE_PATH + "olist_order_payments_dataset.parquet")

print("✅ Dados carregados")

# 🧹 LIMPEZA (exemplo real)
orders = orders[orders["order_status"] == "delivered"]

# 🔗 JOIN (igual SQL)
df = items.merge(orders, on="order_id", how="inner")
df = df.merge(customers, on="customer_id", how="left")
df = df.merge(products, on="product_id", how="left")
df = df.merge(payments, on="order_id", how="left")

print("🔗 JOIN realizado")

# 🧠 TRATAMENTOS
df["order_purchase_timestamp"] = pd.to_datetime(df["order_purchase_timestamp"])

# remover valores inválidos
df = df[df["price"] > 0]

# 📦 salvar Silver
df.to_parquet(SILVER_PATH + "silver_orders.parquet", index=False)

print("🥈 Silver criada com sucesso!")