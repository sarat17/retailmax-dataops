from src.features.crear_variables import es_temporada_alta


def test_temporada_alta_noviembre_y_diciembre():
    assert es_temporada_alta(11) == 1
    assert es_temporada_alta(12) == 1


def test_temporada_normal():
    assert es_temporada_alta(3) == 0


def test_crear_variables_agrega_temporada():
    import pandas as pd
    from src.features.crear_variables import crear_variables

    df = crear_variables(pd.DataFrame({"mes": [12, 3], "es_fin_de_semana": [0, 1]}))
    assert list(df["temporada_alta"]) == [1, 0]
