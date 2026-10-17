# Notebook exportado a .py (sin salidas) - prueba de la variable de temporada
# %%
from src.etl.extraer_ventas import extraer_ventas
from src.features.crear_variables import crear_variables

df = crear_variables(extraer_ventas())
# %%
print(df.groupby("temporada_alta")["unidades"].mean())
