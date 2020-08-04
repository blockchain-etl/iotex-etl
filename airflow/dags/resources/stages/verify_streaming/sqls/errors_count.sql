select if(
(
  select count(1)
  from `{{params.destination_dataset_project_id}}.{{params.dataset_name}}.errors` as errors
  where date(timestamp) >= date_add('{{ds}}', INTERVAL -1 DAY)
) = 0, 1,
cast((select 'Errors table is not empty') as INT64))