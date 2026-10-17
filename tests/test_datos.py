"""Test de Datos: calidad y esquema de los datos de ventas antes de entrenar."""
import pandas as pd
import pytest

RUTA = "data/muestra/ventas_muestra.csv"
COLUMNAS = ["fecha", "pais", "tienda", "mes", "es_fin_de_semana",
            "precio_unitario", "unidades", "ventas"]
PAISES = {"CO", "PE", "CL", "MX", "EC"}


@pytest.fixture(scope="module")
def df():
    return pd.read_csv(RUTA)


def test_esquema_columnas(df):
    assert list(df.columns) == COLUMNAS


def test_nulos_precio_unitario_menor_10(df):
    porcentaje = df["precio_unitario"].isna().mean()
    assert porcentaje <= 0.10, f"{porcentaje:.1%} de nulos en precio_unitario"


def test_precios_y_unidades_positivos(df):
    assert (df["precio_unitario"].dropna() > 0).all()
    assert (df["unidades"] >= 0).all()


def test_paises_validos(df):
    assert set(df["pais"]).issubset(PAISES)
