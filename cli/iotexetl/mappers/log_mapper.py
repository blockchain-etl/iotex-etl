from iotexetl.utils import string_utils


def map_log(block, log):
    return {
        'type': 'log',
        'height': log.blkHeight,
        'action_hash': log.actHash.hex(),
        'contract_address': log.contractAddress,
        'topics': [string_utils.base64_string(topic) for topic in log.topics],
        'data': string_utils.base64_string(log.data),
        'index': log.index,
        'timestamp': block.header.core.timestamp.ToJsonString()
    }