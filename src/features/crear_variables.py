"""Variables para el modelo de predicción de ventas."""
import pandas as pd


def es_temporada_alta(mes: int) -> int:
    """1 si el mes es de temporada alta (Black Friday y Navidad)."""
    return 1 if mes in (11, 12) else 0


def crear_variables(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df["temporada_alta"] = df["mes"].apply(es_temporada_alta)
    return df


COLUMNAS_MODELO = ["mes", "es_fin_de_semana", "temporada_alta"]
