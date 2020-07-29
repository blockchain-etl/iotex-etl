1. Create GCS bucket used for staging and temp location:

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


To rewind subscription to a previous date:

```bash   
for entity in blocks actions logs evm_transfers
do
    gcloud alpha pubsub subscriptions seek \
    projects/iotex-etl-dev/subscriptions/mainnet.dataflow.bigquery.${entity} --time=2020-07-28T23:00:00.000Z
done
```
