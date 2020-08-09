# IoTeX ETL Dataflow

[Apache Beam](https://beam.apache.org/) pipeline for moving IoTeX data from Pub/Sub to BigQuery. 
Deployed in [Google Dataflow](https://cloud.google.com/dataflow).  

## Setting Up

1. Create a GCS bucket used for staging and temp location:

    ```bash
    gcloud config set project <your_gcp_project>
    PROJECT=$(gcloud config get-value project 2> /dev/null)
    ENVIRONMENT_INDEX=0
    BUCKET=${PROJECT}-dataflow-${ENVIRONMENT_INDEX} && echo "${BUCKET}"
    gsutil mb gs://${BUCKET}/
    ```                             
   
2. Create the errors table:

    ```bash
    bq mk --table --description "IoTeX ETL Streaming Errors" \
     ${PROJECT}:mainnet.errors \
     src/main/resources/errors-schema.json 
    ```  
   
3. Update `chainConfigIotexDev.json` with your values.

4. Start the Dataflow job in:

    ```bash
   mvn -e -Pdataflow-runner compile exec:java \
   -Dexec.mainClass=io.blockchainetl.iotex.IotexPubSubToBigQueryPipeline \
   -Dexec.args="--chainConfigFile=chainConfigIotexDev.json \
   --outputErrorsTable=mainnet.errors \
   --tempLocation=gs://${BUCKET}/temp \
   --project=${PROJECT} \
   --runner=DataflowRunner \
   --jobName=iotex-pubsub-to-bigquery-`date +"%Y%m%d-%H%M%S"` \
   --workerMachineType=n1-standard-1 \
   --maxNumWorkers=1 \
   --diskSizeGb=30 \
   --region=us-central1 \
   --zone=us-central1-a \
   " 
   ``` 

To rewind subscriptions to a previous date:

```bash   
for entity in blocks actions logs evm_transfers
do
    gcloud alpha pubsub subscriptions seek \
    projects/iotex-etl-dev/subscriptions/mainnet.dataflow.bigquery.${entity} --time=2020-08-01T23:00:00.000Z
done
```
