# IoTeX ETL Streaming

Streams IoTeX data to [Google Pub/Sub](https://cloud.google.com/pubsub) using 
[iotexetl stream](https://github.com/blockchain-etl/iotex-etl/tree/develop/docs/commands.md#stream). 
Runs in Google Kubernetes Engine. 

Read [this article](https://medium.com/google-cloud/live-ethereum-and-bitcoin-data-in-google-bigquery-and-pub-sub-765b71cd57b5) 
explaining how to subscribe to public blockchain data in [Pub/Sub](https://cloud.google.com/pubsub/docs/overview). 

## Prerequisites

- Kubernetes 1.8+
- Helm 2.16
- PV provisioner support in the underlying infrastructure
- [gcloud](https://cloud.google.com/sdk/install)

## Setting Up

1. Create a GKE cluster:

    ```bash
    gcloud container clusters create iotex-etl-streaming \
    --zone us-central1-a \
    --num-nodes 1 \
    --disk-size 10GB \
    --machine-type n1-standard-1 \
    --network default \
    --subnetwork default \
    --scopes pubsub,storage-rw,logging-write,monitoring-write,service-management,service-control,trace
    
    gcloud container clusters get-credentials iotex-etl-streaming --zone us-central1-a
   
    # Make sure the user has "Kubernetes Engine Admin" role.
    helm init
    bash patch-tiller.sh
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
   
5. Copy [example values](example_values) directory to `values` dir and adjust all the files at least with 
    your bucket and project ID.

6. Install ETL apps via helm using chart from this repo and values we adjust on previous step, for example:

    ```bash
    helm install --name iotex-etl charts/iotex-etl-streaming --values example_values/pubsub/values.yaml
    ``` 

7. Use `describe` command to troubleshoot, f.e.:

    ```bash
    kubectl describe pods
    kubectl describe node [NODE_NAME]
    ```

## Configuration

The following table lists the configurable parameters of the iotex-etl-streaming chart and their default values.

Parameter                                                | Description                                       | Default
-------------------------------------------------------- | ------------------------------------------------- | ----------------------------------------------------------
`stream.image.repository`                                | Stream image source repository name               | `blockchainetl/iotex-etl`
`stream.image.tag`                                       | Image release tag                                 | `1.0.0`
`stream.image.pullPolicy`                                | Image pull policy                                 | `IfNotPresent`
`stream.resources`                                       | CPU/Memory resource request/limit                 | `100m/128Mi, 350m/512Mi`
`stream.env.LAST_SYNCED_BLOCK_FILE_MAX_AGE_IN_SECONDS`   | The number of seconds since new blocks have been pulled from the node, after which the deployment is considered unhealthy                 | `600`
`config.PROVIDER_URI`                                    | URI of IoTeX node                                 | `grpcs://api.mainnet.iotex.one:443`
`config.STREAM_OUTPUT`                                   | Google Pub Sub topic path prefix                  | `projects/<your-project>/topics/crypto_iotex`
`config.GCS_PREFIX`                                      | Google Storage directory of last synced block file| `gs://<your-bucket>/iotex-etl/streaming`
`config.ENTITY_TYPES`                                    | The list of entity types to export                | ``
`config.LAG_BLOCKS`                                      | The number of blocks to lag behind the network    | `10`
`config.MAX_WORKERS`                                     | The number of workers                             | `4`
`lsb_file`                                               | Last synced block file name                       | `last_synced_block.txt`

Alternatively, a YAML file that specifies the values for the parameters can be provided while installing the chart. For example,

```bash
$ helm install --name iotex --values example_values/pubsub/values.yaml charts/iotex-etl-streaming
```