"""Variables para el modelo de predicción de ventas."""
import pandas as pd


def crear_variables(df: pd.DataFrame) -> pd.DataFrame:
    return df.copy()


COLUMNAS_MODELO = ["mes", "es_fin_de_semana"]
