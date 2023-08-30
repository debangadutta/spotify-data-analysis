from datetime import timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago
from datetime import datetime
from spotify_etl import run_spotipy_etl

default_args = {
    'owner' : 'Debanga',
    'depends_on_past' : False,
    'start_date' : datetime(2023,8,30),
    'email' : ['airflow@example.com'],
    'email_on_failure' : False,
    'email_on_retry' : False,
    'retries' : 1,
    'retry_delay' : timedelta(minutes=1)
}

dag = DAG(
    'dag_spotify',
    default_args = default_args,
    description = 'Spotify DAG to fetch the song information from the album Hybrid Theory by Linkin Park'
)

run_etl = PythonOperator(
    task_id  = 'complete_spotify_etl',
    python_callable = run_spotipy_etl,
    dag = dag
)

run_etl