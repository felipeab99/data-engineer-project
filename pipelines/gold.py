import pandas as pd
import os

SILVER_PATH = "data/silver/"
GOLD_PATH = "data/gold/"

os.makedirs(GOLD_PATH, exist_ok=True)

# 📥 carregar silver
df = pd.read_parquet(SILVER_PATH + "silver_orders.parquet")

print("✅ Silver carregado")

# 📅 criar coluna de data
df["data"] = df["order_purchase_timestamp"].dt.date

# 💰 MÉTRICAS
gold = df.groupby("data").agg(
    receita=("price", "sum"),
    pedidos=("order_id", "nunique")
).reset_index()

# 🎯 ticket médio
gold["ticket_medio"] = gold["receita"] / gold["pedidos"]

# 📦 salvar
gold.to_parquet(GOLD_PATH + "gold_vendas.parquet", index=False)

print("🥇 Gold criada com sucesso!")