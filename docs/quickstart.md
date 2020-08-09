# Quickstart

Install IoTeX ETL CLI:

```bash
pip install iotex-etl
```

Export blocks, actions, receipts and logs ([Schema](schema.md), [Reference](commands.md#export_blocks)):

```bash
iotexetl export_blocks --start-block 1 --end-block 100 \
--provider-uri grpcs://api.mainnet.iotex.one:443 --output-dir output
```

Find all commands [here](commands.md).
