# Commands

All commands accept `-h` parameter for help, e.g.:

```bash
iotexetl export_blocks -h

Usage: iotexetl export_blocks [OPTIONS]

  Export blocks, actions, receipts and logs.

Options:
  -s, --start-block INTEGER       Start block  [default: 0]
  -e, --end-block INTEGER         End block  [required]
  -p, --provider-uri TEXT         The URI of the remote IoTeX node  [default:
                                  grpcs://api.mainnet.iotex.one:443]
  -w, --max-workers INTEGER       The maximum number of workers.  [default: 5]
  -b, --batch-size INTEGER        The number of blocks to export in batch. [default: 10]
  -o, --output-dir TEXT           The output directory for block data.
  -h, --help                      Show this message and exit.
```

#### export blocks

```bash
iotexetl export_blocks --start-block 1 --end-block 100 \
--provider-uri grpcs://api.mainnet.iotex.one:443 --output-dir output 
```

Exports blocks, actions, receipts, and logs to individual files in the folder specified in `--output-dir`.

```
Options:
  -s, --start-block INTEGER       Start block  [default: 0]
  -e, --end-block INTEGER         End block  [required]
  -p, --provider-uri TEXT         The URI of the remote IoTex node  [default:
                                  grpcs://api.mainnet.iotex.one:443]
  -w, --max-workers INTEGER       The maximum number of workers.  [default: 5]
  -b, --batch-size INTEGER        How many blocks to batch in single request. [default: 10]
  -o, --output-dir TEXT           The output directory for block data.
  -f, --output-format [json]      The output format.  [default: json]
  -h, --help                      Show this message and exit.
```

#### export transaction logs

```bash
iotexetl export_transaction_logs --start-block 1 --end-block 100 \
--provider-uri grpcs://api.mainnet.iotex.one:443 --output-dir output 
```

Exports transaction logs to file in folder specified in `--output-dir`.

```
Options:
  -s, --start-block INTEGER       Start block  [default: 0]
  -e, --end-block INTEGER         End block  [required]
  -p, --provider-uri TEXT         The URI of the remote IoTex node  [default:
                                  grpcs://api.mainnet.iotex.one:443]
  -w, --max-workers INTEGER       The maximum number of workers.  [default: 5]
  -b, --batch-size INTEGER        How many blocks to batch in single request. [default: 10]
  -o, --output-dir TEXT           The output directory for block data.
  -f, --output-format [json]      The output format.  [default: json]
  -h, --help                      Show this message and exit.
```

#### get_block_range_for_date

```bash
iotexetl get_block_range_for_date --provider-uri=grpcs://api.mainnet.iotex.one:443 --date 2020-07-01
5666159,5683435
```

Outputs start and end blocks for given date.

```
Options:
  -p, --provider-uri TEXT  The URI of the remote IoTeX node  [default:
                           grpcs://api.mainnet.iotex.one:443]
  -d, --date YYYY-MM-DD    The date e.g. 2020-01-01.  [required]
  -o, --output TEXT        The output file. If not specified stdout is used.
  -h, --help               Show this message and exit.
```

#### stream

```bash
iotexetl stream --provider-uri=grpcs://api.mainnet.iotex.one:443
```

Streams all data types to console or Google Pub/Sub.

```
Options:
  -l, --last-synced-block-file TEXT  The text file containing last synced block.  
                                     [default: last_synced_block.txt]
  --lag INTEGER                      The number of blocks to lag behind the
                                     network.  [default: 0]
  -p, --provider-uri TEXT            The URI of the remote IoTeX node.  [default:
                                     grpcs://api.mainnet.iotex.one:443]
  -o, --output TEXT                  Either Google PubSub topic path e.g.
                                     projects/your-project/topics/mainnet
                                     If not specified will print to console.
  -s, --start-block INTEGER          Start block
  -e, --entity-types TEXT            The list of entity types to export.
                                     [default: ,]
  --period-seconds INTEGER           How many seconds to sleep between syncs
                                     [default: 10]
  -b, --batch-size INTEGER           How many blocks to batch in single request
                                     [default: 10]
  -B, --block-batch-size INTEGER     How many blocks to batch in single sync
                                     round  [default: 1]
  -w, --max-workers INTEGER          The number of workers  [default: 5]
  --log-file TEXT                    Log file
  --pid-file TEXT                    pid file
  -h, --help                         Show this message and exit.
```
