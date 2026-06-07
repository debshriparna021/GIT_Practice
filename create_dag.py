from datetime import datetime

@dag(
    dag_id="dag with python operator",
    startdate=datetime(2026,1,1),
    catchup=false,
    scheduele=None,
)

def tutorial_python_operator():
    @task()
    def get_name():
        print("My Name is Shriparna")

    get_name()


tutorial_python_operator()