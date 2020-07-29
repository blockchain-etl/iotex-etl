1. Create GCS bucket used for staging and temp location:

    ```bash
    gcloud config set project <your_gcp_project>
    PROJECT=$(gcloud config get-value project 2> /dev/null)
    ENVIRONMENT_INDEX=0
    BUCKET=${PROJECT}-dataflow-${ENVIRONMENT_INDEX} && echo "${BUCKET}"
    gsutil mb gs://${BUCKET}/
    ```
