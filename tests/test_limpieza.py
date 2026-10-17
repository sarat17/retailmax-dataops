from src.etl.limpiar_clientes import email_valido, limpiar_documento, limpiar_nombre


def test_documento_sin_puntos_ni_guiones():
    assert limpiar_documento("1.023.456-789") == "1023456789"


def test_email_valido():
    assert email_valido("Ana@Mail.com")
    assert not email_valido("ana-sin-arroba.com")


def test_nombre_sin_espacios_de_mas():
    assert limpiar_nombre("  juan   perez ") == "Juan Perez"
