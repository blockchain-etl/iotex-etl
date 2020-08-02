# IoTeX ETL Streaming

Streams the following IoTeX entities to Pub/Sub or Console using 
[iotex-etl stream](https://github.com/blockchain-etl/iotex-etl/tree/develop/docs/commands.md#stream):

- blocks
- actions
- receipts
- logs
- evm_transfers

## Deployment Instructions

1. Create a cluster:

```bash
gcloud container clusters create iotex-etl-streaming \
--zone us-central1-a \
--num-nodes 1 \
--disk-size 10GB \
--machine-type custom-2-4096 \
--network default \
--subnetwork default \
--scopes pubsub,storage-rw,logging-write,monitoring-write,service-management,service-control,trace
```

2. Get `kubectl` credentials:

```bash
gcloud container clusters get-credentials iotex-etl-streaming \
--zone us-central1-a
```

3. Create Pub/Sub topics (use `create_pubsub_topics_iotex.sh`). Skip this step if you need to stream to Console.
  - "mainnet.blocks" 
  - "mainnet.actions" 
  - "mainnet.evm_transfers" 
  - "mainnet.logs" 

4. Create GCS bucket. Upload a text file with block number you want to start streaming from to 
`gs:/<YOUR_BUCKET_HERE>/iotex-etl/streaming/last_synced_block.txt`.

5. Create "iotex-etl-app" service account with roles:
    - Pub/Sub Editor
    - Storage Object Admin

Download the key. Create a Kubernetes secret:

```bash
kubectl create secret generic streaming-app-key --from-file=key.json=$HOME/Downloads/key.json
```

6. Install [helm] (https://github.com/helm/helm#install) 

```bash
brew install helm
```
7. Copy [example values](example_values) directory to `values` dir and adjust all the files at least with your bucket and project ID.
8. Install ETL apps via helm using chart from this repo and values we adjust on previous step, for example:
```bash
helm install iotex-etl charts/iotex-etl-streaming \ 
--values example_values/pubsub/values.yaml

``` 

9. Use `describe` command to troubleshoot, f.e.:

```bash
kubectl describe pods
kubectl describe node [NODE_NAME]
```
