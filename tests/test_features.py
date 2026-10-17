import pandas as pd

from src.features.crear_variables import COLUMNAS_MODELO, crear_variables


def test_crear_variables_no_modifica_original():
    df = pd.DataFrame({"mes": [1], "es_fin_de_semana": [0]})
    crear_variables(df)
    assert list(df.columns) == ["mes", "es_fin_de_semana"]


def test_columnas_modelo_existen():
    assert "mes" in COLUMNAS_MODELO
