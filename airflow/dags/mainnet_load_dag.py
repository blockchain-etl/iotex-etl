from __future__ import print_function

import logging

from iotexetl_airflow.build_load_dag import build_load_dag
from iotexetl_airflow.variables import read_load_dag_vars

logging.basicConfig()
logging.getLogger().setLevel(logging.DEBUG)

# airflow DAG
DAG = build_load_dag(
    dag_id='mainnet_load_dag',
    chain='mainnet',
    **read_load_dag_vars(
        var_prefix='mainnet_',
        load_schedule_interval='0 2 * * *'
    )
)
