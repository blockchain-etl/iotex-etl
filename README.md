# IoTeX ETL Architecture

![blockchain_etl_architecture.svg](iotex_etl_architecture.svg)

1. The nodes are deployed with Terraform and run in Kubernetes. 
  Refer to these for more details:
    - Template repository for deploying Terraform configurations: https://github.com/blockchain-etl/blockchain-terraform-deployment
    - Terraform configuration files for running blockchain nodes: https://github.com/blockchain-etl/blockchain-terraform
    - Kubernetes manifests for running blockchain nodes: https://github.com/blockchain-etl/blockchain-kubernetes

2. The blockchain data is polled periodically from the nodes and pushed to Google Pub/Sub. 
  Refer to these for more details:
    - Article explaining how to subscribe to public blockchain data in Pub/Sub: 
  https://medium.com/google-cloud/live-ethereum-and-bitcoin-data-in-google-bigquery-and-pub-sub-765b71cd57b5 
    - Streaming blockchain data to Google Pub/Sub in Kubernetes: 
  https://github.com/blockchain-etl/iotex-etl/streaming
    - CLI tools for polling blockchain data from nodes: 
  https://github.com/blockchain-etl/iotex-etl/cli. 

3. Airflow DAGs export and load blockchain data to BigQuery daily. 
  Refer to these for more details:
    - Article explaining how the DAGs work: 
  https://cloud.google.com/blog/products/data-analytics/ethereum-bigquery-how-we-built-dataset.
    - Airflow DAGs for exporting, loading, and parsing blockchain data: 
  https://github.com/blockchain-etl/iotex-etl/airflow.
  
4. The blockchain data is pulled from Pub/Sub, transformed and streamed to BigQuery.
  Refer to these for more details:
    - Dataflow pipelines for connecting Pub/Sub topics with BigQuery tables: 
  https://github.com/blockchain-etl/iotex-etl/dataflow.
 