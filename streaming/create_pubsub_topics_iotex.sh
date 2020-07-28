#!/usr/bin/env bash

gcloud deployment-manager deployments create iotex-etl-pubsub-0 --template deployment_manager_pubsub_iotex.py
