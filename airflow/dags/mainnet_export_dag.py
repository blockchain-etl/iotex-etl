from __future__ import print_function

from iotexetl_airflow.build_export_dag import build_export_dag
from iotexetl_airflow.variables import read_export_dag_vars

# airflow DAG
DAG = build_export_dag(
    dag_id='mainnet_export_dag',
    **read_export_dag_vars(
        var_prefix='mainnet_',
        export_schedule_interval='0 1 * * *',
        export_start_date='2019-04-22',
        export_max_active_runs=3,
        export_max_workers=10,
    )
)
