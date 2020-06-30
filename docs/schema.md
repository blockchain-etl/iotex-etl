### blocks

```
version: INTEGER
height: INTEGER
timestamp: TIMESTAMP
prev_block_hash: STRING
tx_root: STRING
delta_state_digest: STRING
receipt_root: STRING
producer_pubkey: STRING
signature: STRING
```

### transfer_actions

```
version: INTEGER
nonce: INTEGER
gas_limit: INTEGER
gas_price: STRING
amount
recipient
payload
```

### execution_actions

```
version: INTEGER
nonce: INTEGER
gas_limit: INTEGER
gas_price: STRING
amount
contract
data
```

### logs

### evm_transfers