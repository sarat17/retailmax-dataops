"""Muestra las métricas del último modelo entrenado."""
import json

if __name__ == "__main__":
    print(json.dumps(json.load(open("modelo/metricas.json")), indent=2))
