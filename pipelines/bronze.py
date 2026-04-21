import pandas as pd
import os

RAW_PATH = "data/raw/"
BRONZE_PATH = "data/bronze/"

os.makedirs(BRONZE_PATH, exist_ok=True)

files = [f for f in os.listdir(RAW_PATH) if f.endswith(".csv")]

for file in files:
    path = RAW_PATH + file
    
    print(f"📥 Lendo {file}...")
    
    df = pd.read_csv(path)
    
    name = file.replace(".csv", ".parquet")
    
    df.to_parquet(BRONZE_PATH + name, index=False)
    
    print(f"✅ {file} salvo como {name}")