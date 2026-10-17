"""DAG de Airflow: consolida el dato maestro Cliente cada noche."""
from datetime import datetime

from airflow import DAG
from airflow.operators.empty import EmptyOperator

with DAG(dag_id="mdm_clientes", start_date=datetime(2026, 1, 1), schedule="0 1 * * *", catchup=False) as dag:
    pasos = [EmptyOperator(task_id=t) for t in
             ["extraer_fuentes", "limpiar", "unir_duplicados", "controles_calidad", "publicar_registro_maestro", "sincronizar"]]
    for a, b in zip(pasos, pasos[1:]):
        a >> b
