# IoTeX ETL CLI

[![Build Status](https://travis-ci.org/blockchain-etl/iotex-etl.svg?branch=master)](https://travis-ci.org/blockchain-etl/iotex-etl)
[![Telegram](https://img.shields.io/badge/telegram-join%20chat-blue.svg)](https://t.me/joinchat/GsMpbA3mv1OJ6YMp3T5ORQ)

IoTeX ETL CLI lets you convert IoTeX data into JSON newline-delimited format.

[Full documentation available here](http://iotex-etl.readthedocs.io/).

## Quickstart

Install IoTeX ETL CLI:

```bash
pip3 install iotex-etl
```

Export blocks, actions and logs ([Schema](../docs/schema.md), [Reference](../docs/commands.md)):

```bash
> iotexetl export_blocks --start-block 1 --end-block 500000 \
--output-dir output --provider-uri grpcs://api.mainnet.iotex.one:443
```

---

Stream blocks, actions and logs to console ([Reference](../docs/commands.md#stream)):

```bash
> pip3 install iotex-etl[streaming]
> iotexetl stream --start-block 500000 -e block,action,log --log-file log.txt \
--provider-uri grpcs://api.mainnet.iotex.one:443
```

Find other commands [here](https://iotex-etl.readthedocs.io/en/latest/commands/).

For the latest version, check out the repo and call 
```bash
> pip3 install -e . 
> python3 iotexetl.py
```

## Useful Links

- [Schema](https://iotex-etl.readthedocs.io/en/latest/schema/)
- [Command Reference](https://iotex-etl.readthedocs.io/en/latest/commands/)
- [Documentation](https://iotex-etl.readthedocs.io/)

## Running Tests

```bash
> pip3 install -e .[dev,streaming]
> export IOTEXETL_PROVIDER_URI=grpcs://api.mainnet.iotex.one:443
> pytest -vv
```

### Running Tox Tests

```bash
> pip3 install tox
> tox
```

## Running in Docker

1. Install Docker https://docs.docker.com/install/

2. Build a docker image
        
        > docker build -t iotex-etl:latest .
        > docker image ls
        
3. Run a container out of the image

        > docker run -v $HOME/output:/iotex-etl/output iotex-etl:latest export_blocks -s 1 -e 5499999 -b 1000 -o out

4. Run streaming to console or Pub/Sub

        > docker build -t iotex-etl:latest -f Dockerfile .
        > echo "Stream to console"
        > docker run iotex-etl:latest stream --start-block 500000 --log-file log.txt
        > echo "Stream to Pub/Sub"
        > docker run -v /path_to_credentials_file/:/iotex-etl/ --env GOOGLE_APPLICATION_CREDENTIALS=/iotex-etl/credentials_file.json iotex-etl:latest stream --start-block 500000 --output projects/<your-project>/topics/mainnet
