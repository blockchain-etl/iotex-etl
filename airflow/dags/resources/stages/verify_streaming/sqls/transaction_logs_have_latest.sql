select if(
(
select timestamp_diff(
  current_timestamp(),
  (select max(timestamp)
  from `{{params.destination_dataset_project_id}}.{{params.dataset_name}}.transaction_logs` as transaction_logs
  where date(timestamp) >= date_add('{{ds}}', INTERVAL -1 DAY)),
  MINUTE)
) < {{params.max_lag_in_minutes}}, 1,
cast((select 'Transaction logs are lagging by more than {{params.max_lag_in_minutes}} minutes') as INT64))
