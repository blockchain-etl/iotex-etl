#!/usr/bin/env bash

mvn -e -Pdataflow-runner compile exec:java \
-Dexec.mainClass=io.blockchainetl.iotex.IotexPubSubToBigQueryPipeline \
-Dexec.args="--chainConfigFile=chainConfigIotexDev.json \
--tempLocation=gs://iotex-etl-dev-dataflow-0/temp \
--project=iotex-etl-dev \
--runner=DataflowRunner \
--jobName=iotex-pubsub-to-bigquery-0 \
--workerMachineType=n1-standard-1 \
--maxNumWorkers=1 \
--diskSizeGb=30 \
--region=us-central1 \
--zone=us-central1-a \
"
