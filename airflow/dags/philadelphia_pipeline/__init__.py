from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

from . import fetch_data
from . import transform_data
from . import render_report

with DAG(dag_id='jawnt_philadelphia_pipeline',
         schedule_interval='@daily',
         catchup=False) as dag:

    extract_raw_addresses = PythonOperator(
        task_id='fetch_data',
        python_callable=fetch_data.main,
    )

    extract_geocoded_addresses = PythonOperator(
        task_id='transform_data',
        python_callable=transform_data.main,
    )

    load_address_data = PythonOperator(
        task_id='render_report',
        python_callable=render_report.main,
    )

    extract_raw_addresses >> extract_geocoded_addresses >> load_address_data
