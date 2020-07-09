### blocks

Column             | Type               |
-------------------|--------------------|
version            | INTEGER            |
height             | INTEGER            |
timestamp          | TIMESTAMP          |
prev_block_hash    | STRING             |
tx_root            | STRING             |
receipt_root       | STRING             |
delta_state_digest | STRING             |
producer_pubkey    | STRING             |
signature          | STRING             |

### actions

| Column                                                      | Type              |
|-------------------------------------------------------------|-------------------|
| hash                                                        | STRING            |
| height                                                      | INTEGER           |
| timestamp                                                   | TIMESTAMP         |
| action_type                                                 | STRING            |
| sender_pub_key                                              | STRING            |
| version                                                     | INTEGER           |
| nonce                                                       | INTEGER           |
| gas_limit                                                   | INTEGER           |
| gas_price                                                   | INTEGER           |
| status                                                      | INTEGER           |
| gas_consumed                                                | INTEGER           |
| contract_address                                            | STRING            |
| transfer                                                    | STRUCT            |
| transfer.amount                                             | STRING            |
| transfer.recipient                                          | STRING            |
| transfer.payload                                            | STRING            |
| execution                                                   | STRUCT            |
| execution.amount                                            | STRING            |
| execution.contract                                          | STRING            |
| execution.data                                              | STRING            |
| start_sub_chain                                             | STRUCT            |
| start_sub_chain.chain_id                                    | INTEGER           |
| start_sub_chain.security_deposit                            | STRING            |
| start_sub_chain.operation_deposit                           | STRING            |
| start_sub_chain.start_height                                | STRING            |
| start_sub_chain.parent_height_offset                        | STRING            |
| stop_sub_chain                                              | STRUCT            |
| stop_sub_chain.chain_id                                     | INTEGER           |
| stop_sub_chain.stop_height                                  | INTEGER           |
| stop_sub_chain.sub_chain_address                            | STRING            |
| put_block                                                   | STRUCT            |
| put_block.sub_chain_address                                 | STRING            |
| put_block.height                                            | INTEGER           |
| put_block.roots                                             | STRUCT (REPEATED) |
| put_block.roots.name                                        | STRING            |
| put_block.roots.value                                       | STRING            |
| create_deposit                                              | STRUCT            |
| create_deposit.chain_id                                     | INTEGER           |
| create_deposit.amount                                       | STRING            |
| create_deposit.recipient                                    | STRING            |
| settle_deposit                                              | STRUCT            |
| settle_deposit.amount                                       | STRING            |
| settle_deposit.recipient                                    | STRING            |
| settle_deposit.index                                        | INTEGER           |
| terminate_plum_chain                                        | STRUCT            |
| terminate_plum_chain.sub_chain_address                      | STRING            |
| sub_chain_address                                           | STRING            |
| plum_put_block                                              | STRUCT            |
| plum_put_block.height                                       | INTEGER           |
| plum_put_block.roots                                        | STRUCT (REPEATED) |
| plum_put_block.roots.name                                   | STRING            |
| plum_put_block.roots.value                                  | STRING            |
| plum_create_deposit                                         | STRUCT            |
| plum_create_deposit.sub_chain_address                       | STRING            |
| plum_create_deposit.amount                                  | STRING            |
| plum_create_deposit.recipient                               | STRING            |
| plum_start_exit                                             | STRUCT            |
| plum_start_exit.sub_chain_address                           | STRING            |
| plum_start_exit.previous_transfer                           | STRING            |
| plum_start_exit.previous_transfer_block_proof               | STRING            |
| plum_start_exit.previous_transfer_block_height              | INTEGER           |
| plum_start_exit.exit_transfer                               | INTEGER           |
| plum_start_exit.exit_transfer_block_proof                   | STRING            |
| plum_start_exit.exit_transfer_block_height                  | INTEGER           |
| plum_challenge_exit                                         | STRUCT            |
| plum_challenge_exit.sub_chain_address                       | STRING            |
| plum_challenge_exit.coin_id                                 | INTEGER           |
| plum_challenge_exit.challenge_transfer                      | STRING            |
| plum_challenge_exit.challenge_transfer_block_proof          | STRING            |
| plum_challenge_exit.challenge_transfer_block_height         | STRING            |
| plum_response_challenge_exit                                | STRUCT            |
| plum_response_challenge_exit.sub_chain_address              | STRING            |
| plum_response_challenge_exit.coin_id                        | INTEGER           |
| plum_response_challenge_exit.challenge_transfer             | STRING            |
| plum_response_challenge_exit.response_transfer              | STRING            |
| plum_response_challenge_exit.response_transfer_block_proof  | STRING            |
| plum_response_challenge_exit.previous_transfer_block_height | INTEGER           |
| plum_finalize_exit                                          | STRUCT            |
| plum_finalize_exit.sub_chain_address                        | STRING            |
| plum_finalize_exit.coin_id                                  | INTEGER           |
| plum_settle_deposit                                         | STRUCT            |
| plum_settle_deposit.coin_id                                 | INTEGER           |
| plum_transfer                                               | STRUCT            |
| plum_transfer.coin_id                                       | INTEGER           |
| plum_transfer.denomination                                  | STRING            |
| plum_transfer.owner                                         | STRING            |
| plum_transfer.recipient                                     | STRING            |
| deposit_to_rewarding_fund                                   | STRUCT            |
| deposit_to_rewarding_fund.amount                            | STRING            |
| deposit_to_rewarding_fund.data                              | STRING            |
| claim_from_rewarding_fund                                   | STRUCT            |
| claim_from_rewarding_fund.amount                            | STRING            |
| claim_from_rewarding_fund.data                              | STRING            |
| grant_reward                                                | STRUCT            |
| grant_reward.type                                           | INTEGER           |
| grant_reward.height                                         | INTEGER           |
| stake_create                                                | STRUCT            |
| stake_create.candidate_name                                 | STRING            |
| stake_create.staked_amount                                  | STRING            |
| stake_create.staked_duration                                | INTEGER           |
| stake_create.auto_stake                                     | BOOLEAN           |
| stake_create.payload                                        | STRING            |
| stake_unstake                                               | STRUCT            |
| stake_unstake.bucket_index                                  | INTEGER           |
| stake_unstake.payload                                       | STRING            |
| stake_withdraw                                              | STRUCT            |
| stake_withdraw.bucket_index                                 | INTEGER           |
| stake_withdraw.payload                                      | STRING            |
| stake_add_deposit                                           | STRUCT            |
| stake_add_deposit.bucket_index                              | INTEGER           |
| stake_add_deposit.amount                                    | STRING            |
| stake_add_deposit.payload                                   | STRING            |
| stake_restake                                               | STRUCT            |
| stake_restake.bucket_index                                  | INTEGER           |
| stake_restake.staked_duration                               | INTEGER           |
| stake_restake.auto_stake                                    | BOOLEAN           |
| stake_restake.payload                                       | STRING            |
| stake_change_candidate                                      | STRUCT            |
| stake_change_candidate.bucket_index                         | INTEGER           |
| stake_change_candidate.candidate_name                       | STRING            |
| stake_change_candidate.payload                              | STRING            |
| stake_transfer_ownership                                    | STRUCT            |
| stake_transfer_ownership.bucket_index                       | INTEGER           |
| stake_transfer_ownership.voter_address                      | STRING            |
| stake_transfer_ownership.payload                            | STRING            |
| candidate_register                                          | STRUCT            |
| candidate_register.name                                     | STRING            |
| candidate_register.operator_address                         | STRING            |
| candidate_register.reward_address                           | STRING            |
| candidate_register.staked_amount                            | STRING            |
| candidate_register.staked_duration                          | INTEGER           |
| candidate_register.auto_stake                               | BOOLEAN           |
| candidate_register.owner_address                            | STRING            |
| candidate_register.payload                                  | STRING            |
| candidate_basic_info                                        | STRUCT            |
| candidate_basic_info.name                                   | STRING            |
| candidate_basic_info.operator_address                       | STRING            |
| candidate_basic_info.reward_address                         | STRING            |
| put_poll_result                                             | STRUCT            |
| put_poll_result.height                                      | INTEGER           |
| put_poll_result.candidates                                  | STRUCT (REPEATED) |
| put_poll_result.candidates.address                          | STRING            |
| put_poll_result.candidates.votes                            | STRING            |
| put_poll_result.candidates.pub_key                          | STRING            |
| put_poll_result.candidates.reward_address                   | STRING            |

### logs

Column            | Type               |
------------------|--------------------|
height            | INTEGER            |
timestamp         | TIMESTAMP          |
action_hash       | STRING             |
contract_address  | STRING             |
topics            | STRING (REPEATED)  |
data              | STRING             |
blk_height        | INTEGER            |
act_hash          | STRING             |
index             | INTEGER            |

### evm_transfers

Column            | Type               |
------------------|--------------------|
height            | INTEGER            |
timestamp         | TIMESTAMP          |
action_hash       | STRING             |
amount            | STRING             |
from              | STRING             |
to                | STRING             |
index             | INTEGER            |