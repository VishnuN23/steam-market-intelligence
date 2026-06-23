import pandas as pd

df = pd.read_csv("data/raw/merged_data.csv")

print("\n=== COLUMNS ===")

print(df.columns.tolist())

print("\n=== SHAPE ===")
print(df.shape)

print("\n=== MISSING VALUES ===")
print(df.isnull().sum())