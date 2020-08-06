# IoTeX ETL Streaming

Streams IoTeX data to [Google Pub/Sub](https://cloud.google.com/pubsub) using 
[iotexetl stream](https://github.com/blockchain-etl/iotex-etl/tree/develop/docs/commands.md#stream). 
Runs in Google Kubernetes Engine. 

Read [this article](https://medium.com/google-cloud/live-ethereum-and-bitcoin-data-in-google-bigquery-and-pub-sub-765b71cd57b5) 
explaining how to subscribe to public blockchain data in [Pub/Sub](https://cloud.google.com/pubsub/docs/overview). 

## Setting Up

1. Create a GKE cluster:

    ```bash
    gcloud container clusters create iotex-etl-streaming \
    --zone us-central1-a \
    --num-nodes 1 \
    --disk-size 10GB \
    --machine-type custom-2-4096 \
    --network default \
    --subnetwork default \
    --scopes pubsub,storage-rw,logging-write,monitoring-write,service-management,service-control,trace
   
   gcloud container clusters get-credentials iotex-etl-streaming --zone us-central1-a
    ```

2. Create Pub/Sub topics and subscriptions:

    ```bash
   gcloud deployment-manager deployments create iotex-etl-pubsub-0 --template deployment_manager_pubsub_iotex.py 
   ```

3. Create GCS bucket. Upload a text file with block number you want to start streaming from to 
`gs:/<YOUR_BUCKET_HERE>/iotex-etl/streaming/last_synced_block.txt`.

4. Create "iotex-etl-app" service account with roles:
    - Pub/Sub Editor
    - Storage Object Admin

    Download the key. Create a Kubernetes secret:

    ```bash
    kubectl create secret generic streaming-app-key --from-file=key.json=$HOME/Downloads/key.json
    ```

5. Install [helm] (https://github.com/helm/helm#install) 

    ```bash
    brew install helm
    ```
   
6. Copy [example values](example_values) directory to `values` dir and adjust all the files at least with 
    your bucket and project ID.

7. Install ETL apps via helm using chart from this repo and values we adjust on previous step, for example:

    ```bash
    helm install iotex-etl charts/iotex-etl-streaming \ 
    --values example_values/pubsub/values.yaml
    ``` 

8. Use `describe` command to troubleshoot, f.e.:

    ```bash
    kubectl describe pods
    kubectl describe node [NODE_NAME]
    ```
