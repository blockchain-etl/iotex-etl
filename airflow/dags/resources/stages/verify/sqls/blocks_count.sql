SELECT IF(
(
    SELECT MAX(height)
    FROM `{{params.destination_dataset_project_id}}.{{params.dataset_name}}.blocks`
    WHERE DATE(TIMESTAMP) <= '{{ds}}'
) =
(
    SELECT COUNT(*) FROM `{{params.destination_dataset_project_id}}.{{params.dataset_name}}.blocks`
    WHERE DATE(TIMESTAMP) <= '{{ds}}'
), 1,
CAST((SELECT 'Total number of blocks is not equal to last block number {{ds}}') AS INT64))
