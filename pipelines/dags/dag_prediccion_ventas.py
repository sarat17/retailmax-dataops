"""DAG de Airflow: reentrena el modelo de predicción de ventas cada lunes."""
from datetime import datetime

from airflow import DAG
from airflow.operators.bash import BashOperator

with DAG(
    dag_id="prediccion_ventas",
    start_date=datetime(2026, 1, 1),
    schedule="0 3 * * 1",
    catchup=False,
    tags=["retailmax", "ventas"],
) as dag:
    extraer = BashOperator(task_id="extraer_ventas", bash_command="python -m src.etl.extraer_ventas")
    test_datos = BashOperator(task_id="test_de_datos", bash_command="pytest tests/test_datos.py")
    entrenar = BashOperator(task_id="entrenar_y_validar", bash_command="python -m src.models.entrenar_prediccion_ventas")

    extraer >> test_datos >> entrenar
