# transform/excel_para_csv.py
import pandas as pd
import os

# Caminhos de entrada e saída
arquivo_excel = "dados/raw/sample1.xlsx"
arquivo_csv = "dados/processed/sample1.csv"

# Garante que a pasta de saída exista
os.makedirs("dados/processed", exist_ok=True)

# Leitura e transformação
df = pd.read_excel(arquivo_excel)
df.to_csv(arquivo_csv, index=False)

print(f"Transformação concluída: {arquivo_csv}")
