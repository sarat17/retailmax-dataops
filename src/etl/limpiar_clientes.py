"""Reglas de limpieza del dato maestro Cliente (ver docs/gobernanza_cliente.md)."""
import re


def limpiar_documento(documento: str) -> str:
    """Deja el documento sin puntos, guiones ni espacios."""
    return re.sub(r"[^0-9A-Za-z]", "", str(documento))


def limpiar_email(email: str) -> str:
    return str(email).strip().lower()


def email_valido(email: str) -> bool:
    return re.fullmatch(r"[^@\s]+@[^@\s]+\.[^@\s]+", limpiar_email(email)) is not None


def limpiar_nombre(nombre: str) -> str:
    return " ".join(str(nombre).split()).title()
