### blocks

Column             | Type               |
-------------------|--------------------|
version            | INTEGER            |
height             | INTEGER            |
timestamp          | TIMESTAMP          |
prev_block_hash    | STRING             |
tx_root            | STRING             |
delta_state_digest | STRING             |
receipt_root       | STRING             |
logsBloom          | STRING             |
producer_pubkey    | STRING             |
signature          | STRING             |

### transfer_actions

Column            | Type               |
------------------|--------------------|
version           | INTEGER            |
nonce             | INTEGER            |
gas_limit         | INTEGER            |
gas_price         | STRING             |
amount            | STRING             |
recipient         | STRING             |
payload           | STRING             |

### execution_actions

Column            | Type               |
------------------|--------------------|
version           | INTEGER            |
nonce             | INTEGER            |
gas_limit         | INTEGER            |
gas_price         | STRING             |
amount            | STRING             |
contract          | STRING             |
data              | STRING             |

### start_sub_chain_actions

Column               | Type               |
---------------------|--------------------|
version              | INTEGER            |
nonce                | INTEGER            |
gas_limit            | INTEGER            |
gas_price            | STRING             |
chain_id             | INTEGER            |
security_deposit     | STRING             |
operation_deposit    | STRING             |
start_height         | STRING             |
parent_height_offset | STRING             |

### stop_sub_chain_actions

Column            | Type               |
------------------|--------------------|
version           | INTEGER            |
nonce             | INTEGER            |
gas_limit         | INTEGER            |
gas_price         | STRING             |
chain_id          | INTEGER            |
stop_height       | INTEGER            |
sub_chain_address | STRING             |

### put_block_actions

Column            | Type               |
------------------|--------------------|
version           | INTEGER            |
nonce             | INTEGER            |
gas_limit         | INTEGER            |
gas_price         | STRING             |
sub_chain_address | STRING             |
height            | INTEGER            |

### merkle_root

Column            | Type               |
------------------|--------------------|
name              | STRING             |
value             | STRING             |

### create_deposit_actions

Column            | Type               |
------------------|--------------------|
version           | INTEGER            |
nonce             | INTEGER            |
gas_limit         | INTEGER            |
gas_price         | STRING             |
chain_id          | INTEGER            |
amount            | STRING             |
recipient         | STRING             |

### settle_deposit_actions

Column            | Type               |
------------------|--------------------|
version           | INTEGER            |
nonce             | INTEGER            |
gas_limit         | INTEGER            |
gas_price         | STRING             |
amount            | STRING             |
recipient         | STRING             |
index             | INTEGER            |

### create_plum_chain_actions

Column            | Type               |
------------------|--------------------|
version           | INTEGER            |
nonce             | INTEGER            |
gas_limit         | INTEGER            |
gas_price         | STRING             |

### terminate_plum_chain_actions

Column            | Type               |
------------------|--------------------|
version           | INTEGER            |
nonce             | INTEGER            |
gas_limit         | INTEGER            |
gas_price         | STRING             |
sub_chain_address | STRING             |

### plum_put_block_actions

Column            | Type               |
------------------|--------------------|
version           | INTEGER            |
nonce             | INTEGER            |
gas_limit         | INTEGER            |
gas_price         | STRING             |
sub_chain_address | STRING             |
height            | INTEGER            |
roots             |                    |

### plum_create_deposit_actions

Column            | Type               |
------------------|--------------------|
version           | INTEGER            |
nonce             | INTEGER            |
gas_limit         | INTEGER            |
gas_price         | STRING             |
sub_chain_address | STRING             |
amount            | STRING             |
recipient         | STRING             |

### plum_start_exit_actions

Column                         | Type               |
-------------------------------|--------------------|
version                        | INTEGER            |
nonce                          | INTEGER            |
gas_limit                      | INTEGER            |
gas_price                      | STRING             |
sub_chain_address              | STRING             |
previous_transfer              | STRING             |
previous_transfer_block_proof  | STRING             |
previous_transfer_block_height | INTEGER            |
exit_transfer                  | INTEGER            |
exit_transfer_block_proof      | STRING             |
exit_transfer_block_height     | INTEGER            |

### plum_challenge_exit_actions

Column                          | Type               |
--------------------------------|--------------------|
version                         | INTEGER            |
nonce                           | INTEGER            |
gas_limit                       | INTEGER            |
gas_price                       | STRING             |
sub_chain_address               | STRING             |
coin_id                         | INTEGER            |
challenge_transfer              | STRING             |
challenge_transfer_block_proof  | STRING             |
challenge_transfer_block_height | STRING             |

### plum_response_challenge_exit_actions

Column                         | Type               |
-------------------------------|--------------------|
version                        | INTEGER            |
nonce                          | INTEGER            |
gas_limit                      | INTEGER            |
gas_price                      | STRING             |
sub_chain_address              | STRING             |
coin_id                        | INTEGER            |
challenge_transfer             | STRING             |
response_transfer              | STRING             |
response_transfer_block_proof  | STRING             |
previous_transfer_block_height | INTEGER            |

### plum_finalize_exit_actions

Column            | Type               |
------------------|--------------------|
version           | INTEGER            |
nonce             | INTEGER            |
gas_limit         | INTEGER            |
gas_price         | STRING             |
sub_chain_address | STRING             |
coin_id           | INTEGER            |

### plum_settle_deposit_actions

Column            | Type               |
------------------|--------------------|
version           | INTEGER            |
nonce             | INTEGER            |
gas_limit         | INTEGER            |
gas_price         | STRING             
coin_id           | INTEGER            |

### plum_transfer_actions

Column            | Type               |
------------------|--------------------|
version           | INTEGER            |
nonce             | INTEGER            |
gas_limit         | INTEGER            |
gas_price         | STRING             |
coin_id           | INTEGER            |
denomination      | STRING             |
owner             | STRING             |
recipient         | STRING             |

### deposit_to_rewarding_fund_actions

Column            | Type               |
------------------|--------------------|
version           | INTEGER            |
nonce             | INTEGER            |
gas_limit         | INTEGER            |
gas_price         | STRING             |
amount            | STRING             |
data              | STRING             |

### claim_from_rewarding_fund_actions

Column            | Type               |
------------------|--------------------|
version           | INTEGER            |
nonce             | INTEGER            |
gas_limit         | INTEGER            |
gas_price         | STRING             |
amount            | STRING             |
data              | STRING             |

### grant_reward_actions

Column            | Type               |
------------------|--------------------|
version           | INTEGER            |
nonce             | INTEGER            |
gas_limit         | INTEGER            |
gas_price         | STRING             |
type              | INTEGER            |
height            | INTEGER            |

### stake_create_actions

Column            | Type               |
------------------|--------------------|
version           | INTEGER            |
nonce             | INTEGER            |
gas_limit         | INTEGER            |
gas_price         | STRING             |
candidate_name    | STRING             |
staked_amount     | STRING             |
staked_duration   | INTEGER            |
auto_stake        | BOOLEAN            |
payload           | INTEGER            |

### stake_reclaim_actions

Column            | Type               |
------------------|--------------------|
version           | INTEGER            |
nonce             | INTEGER            |
gas_limit         | INTEGER            |
gas_price         | STRING             |
bucket_index      | INTEGER            |
payload           | STRING             |

### stake_add_deposit_actions

Column            | Type               |
------------------|--------------------|
version           | INTEGER            |
nonce             | INTEGER            |
gas_limit         | INTEGER            |
gas_price         | STRING             |
bucket_index      | INTEGER            |
amount            | STRING             |
payload           | STRING             |

### stake_restake_actions

Column            | Type               |
------------------|--------------------|
version           | INTEGER            |
nonce             | INTEGER            |
gas_limit         | INTEGER            |
gas_price         | STRING             |
bucket_index      | INTEGER            |
stakedDuration    | INTEGER            |
autoStake         | BOOLEAN            |
payload           | STRING             |

### stake_change_candidate_actions

Column            | Type               |
------------------|--------------------|
version           | INTEGER            |
nonce             | INTEGER            |
gas_limit         | INTEGER            |
gas_price         | STRING             |
bucket_index      | INTEGER            |
candidate_name    | STRING             |
payload           | STRING             |

### stake_transfer_ownership_actions

Column            | Type               |
------------------|--------------------|
version           | INTEGER            |
nonce             | INTEGER            |
gas_limit         | INTEGER            |
gas_price         | STRING             |
bucket_index      | INTEGER            |
voter_address     | STRING             |
payload           | STRING             |

### candidate_register_actions

Column            | Type               |
------------------|--------------------|
version           | INTEGER            |
nonce             | INTEGER            |
gas_limit         | INTEGER            |
gas_price         | STRING             |
name              | STRING             |
operator_address  | STRING             |
reward_address    | STRING             |
staked_amount     | STRING             |
staked_duration   | INTEGER            |
auto_stake        | BOOLEAN            |
owner_address     | STRING             |
payload           | STRING             |

### candidate_basic_info_actions

Column            | Type               |
------------------|--------------------|
version           | INTEGER            |
nonce             | INTEGER            |
gas_limit         | INTEGER            |
gas_price         | STRING             |
name              | STRING             |
operator_address  | STRING             |
reward_address    | STRING             |

### put_poll_result_actions

Column            | Type               |
------------------|--------------------|
version           | INTEGER            |
nonce             | INTEGER            |
gas_limit         | INTEGER            |
gas_price         | STRING             |
height            | INTEGER            |

### candidate

Column            | Type               |
------------------|--------------------|
address           | STRING             |
votes             | STRING             |
pub_key           | STRING             |
reward_address    | STRING             |

### receipts

Column            | Type               |
------------------|--------------------|
status            | INTEGER            |
blk_height        | INTEGER            |
act_hash          | STRING             |
gas_consumed      | INTEGER            |
contract_address  | STRING             |

### logs

Column            | Type               |
------------------|--------------------|
contract_address  | STRING             |
topics            |                    |
data              | STRING             |
blk_height        | INTEGER            |
act_hash          | STRING             |
index             | INTEGER            |

### evm_transfers

Column            | Type               |
------------------|--------------------|
amount            | STRING             |
from              | STRING             |
to                | STRING             |