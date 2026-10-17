# Notebook exportado a .py (sin salidas) - exploración inicial de ventas
# %%
from src.etl.extraer_ventas import extraer_ventas

df = extraer_ventas()
# %%
print(df.groupby("pais")["ventas"].sum())
