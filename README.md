# IoTeX ETL

[![Build Status](https://travis-ci.org/blockchain-etl/iotex-etl.svg?branch=master)](https://travis-ci.org/blockchain-etl/iotex-etl)
[![Telegram](https://img.shields.io/badge/telegram-join%20chat-blue.svg)](https://t.me/joinchat/GsMpbA3mv1OJ6YMp3T5ORQ)

## Overview

IoTeX ETL allows you to setup an ETL pipeline in Google Cloud Platform for making IoTeX blockchain data available
in BigQuery and Pub/Sub. It comes with [CLI tools](/cli) for exporting IoTeX data into JSON newline-delimited files
partitioned by day. 

Data is available for you to query right away in 
[Google BigQuery](https://console.cloud.google.com/bigquery?page=dataset&d=mainnet&p=iotex-etl).

## Architecture

![iotex_etl_architecture.svg](iotex_etl_architecture.svg)

[Google Slides version](https://docs.google.com/presentation/d/1VFMR4f8lghnpGZWZTevRTv6Zn9n9IUWHRnNrQsNE-8Y/edit#slide=id.p89)

1. The nodes are run in a Kubernetes cluster. 
    Refer to [IoTeX Node in Kubernetes](https://github.com/blockchain-etl/iotex-kubernetes) for deployment instructions.

2. [Airflow DAGs](https://airflow.apache.org/) export and load IoTeX data to BigQuery daily. 
    Refer to [IoTeX ETL Airflow](/airflow) for deployment instructions.
  
3. IoTeX data is polled periodically from the nodes and pushed to Google Pub/Sub. 
    Refer to [IoTeX ETL Streaming](/streaming) for deployment instructions.  
  
4. IoTeX data is pulled from Pub/Sub, transformed and streamed to BigQuery. 
    Refer to [IoTeX ETL Dataflow](/dataflow) for deployment instructions.  
 