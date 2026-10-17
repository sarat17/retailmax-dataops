"""Extrae las ventas desde la fuente (en este repo, el archivo de muestra)."""
import pandas as pd

RUTA_MUESTRA = "data/muestra/ventas_muestra.csv"


def extraer_ventas(ruta: str = RUTA_MUESTRA) -> pd.DataFrame:
    return pd.read_csv(ruta, parse_dates=["fecha"])
