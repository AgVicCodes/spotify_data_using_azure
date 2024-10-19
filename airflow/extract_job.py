import airflow
from airflow.models.dag import DAG111
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
from extract_recent import get_recently_played


default_args = {
        "email": ["victoragbeleye2@gmail.com"],
        "email_on_failure": True,
        "email_on_retry": True,
        "retries": 2,
        "retry_delay": timedelta(minutes = 30)
    }

with DAG (
    "extract_user_recently_played",
    default_args = default_args,
    description = "Extracts API data from user listening history via spotify",
    schedule = "* */12 * * *",
    start_date = datetime(2024, 9, 30),
    tags = ["recently_played"]
) as dag:
    t1 = PythonOperator(
        task_id = "Extract_recent",
        python_callable = get_recently_played,
        dag = dag
    )

t1

# Login with username: admin  password: q39K47TT47GzPqfe