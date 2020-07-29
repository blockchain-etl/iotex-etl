#!/usr/bin/env bash

mvn -Pdirect-runner compile exec:java \
-Dexec.mainClass=io.blockchainetl.iotex.IotexPubSubToBigQueryPipeline \
-Dexec.args="--chainConfigFile=chainConfigIotexDev.json \
--tempLocation=gs://iotex-etl-dev-dataflow-0/ \
--outputErrorsTable=mainnet.errors"

