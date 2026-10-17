"""Entrena y valida el modelo de predicción de unidades vendidas.

El pipeline de CD solo continúa si el error (MAPE) es menor al umbral
definido en config/modelo_ventas.json.
"""
import json
import os
import pickle
import subprocess
import sys

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_percentage_error
from sklearn.model_selection import train_test_split

from src.etl.extraer_ventas import extraer_ventas
from src.features.crear_variables import COLUMNAS_MODELO, crear_variables


def main() -> int:
    config = json.load(open("config/modelo_ventas.json", encoding="utf-8"))
    df = crear_variables(extraer_ventas())
    X, y = df[COLUMNAS_MODELO], df["unidades"]
    X_tr, X_te, y_tr, y_te = train_test_split(
        X, y, test_size=0.25, random_state=config["semilla"]
    )
    modelo = LinearRegression().fit(X_tr, y_tr)
    mape = mean_absolute_percentage_error(y_te, modelo.predict(X_te))

    try:
        commit = subprocess.check_output(["git", "rev-parse", "--short", "HEAD"], stderr=subprocess.DEVNULL).decode().strip()
    except Exception:
        commit = "desconocido"

    os.makedirs("modelo", exist_ok=True)
    pickle.dump(modelo, open("modelo/modelo_ventas.pkl", "wb"))
    metricas = {"mape": round(mape, 4), "umbral": config["mape_maximo"], "commit": commit}
    json.dump(metricas, open("modelo/metricas.json", "w"), indent=2)
    print(f"MAPE del modelo: {mape:.2%} (máximo permitido: {config['mape_maximo']:.0%})")

    if mape > config["mape_maximo"]:
        print("El modelo NO supera el umbral. Se detiene el pipeline.")
        return 1
    print("El modelo supera el umbral. Puede continuar al empaquetado.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
