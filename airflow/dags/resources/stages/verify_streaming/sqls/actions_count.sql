select if(abs(
  coalesce((
      select sum(number_of_actions)
      from `{{params.destination_dataset_project_id}}.{{params.dataset_name}}.blocks` as blocks
      where date(timestamp) = '{{ds}}'
  ),0 ) -
  coalesce((
      select count(*)
      from `{{params.destination_dataset_project_id}}.{{params.dataset_name}}.actions` as actions
      where date(timestamp) = '{{ds}}'
  ), 0)) <
  coalesce((
      select avg(number_of_actions)
      from `{{params.destination_dataset_project_id}}.{{params.dataset_name}}.blocks` as blocks
      where date(timestamp) = '{{ds}}'
  ), 100) * 2, 1,
cast((select 'The difference between number of actions and sum of action_count in blocks table is greater than average action number in a block by more than 2 times') as INT64))
