import os
from airflow import DAG
from airflow.operators.empty import EmptyOperator
from datetime import datetime, timedelta
from airflow.operators.bash import BashOperator
from airflow.models import Variable
import pytz

def python_run(file_name):
    command = (
        "cd /opt/airflow/Python/ && " +
        ". my_project/bin/activate && " +
        "cd code && " +
        "python " + file_name
    )
    return command


with DAG(
    dag_id="data_pipeline",
    catchup=False,
    default_args={
        'owner': 'tung.inda',
        'start_date': datetime(2024, 8, 13, 0, 0, tzinfo=pytz.timezone('Asia/Ho_Chi_Minh')),
        'pool': 'default_pool',
        'retries': 0,
        'retry_delay': timedelta(minutes=2),
        'execution_timeout': timedelta(minutes=50),
    },
    schedule_interval='00 7 * * *',  # Lên lịch chạy vào lúc 7 giờ sáng mỗi ngày theo giờ Việt Nam
) as dag:
    # Call api
    call_api = BashOperator(
        task_id='call_api',
        bash_command=python_run('call_api.py'),
    )
    tranform_to_csv = BashOperator(
        task_id='tranform_csv',
        bash_command=python_run('tranform_to_csv.py'),
    )
    up_load = BashOperator(
        task_id='up_load',
        bash_command=python_run('up_load.py'),
    )
    insert_table = BashOperator(
        task_id='insert_table',
        bash_command=python_run('insert_table.py'),
    )
    # Các task đầu và cuối
    start = EmptyOperator(task_id="start")
    end = EmptyOperator(task_id="end")
    
    # Xác định thứ tự chạy các task
    start >> call_api >> tranform_to_csv >> up_load >> insert_table >> end
