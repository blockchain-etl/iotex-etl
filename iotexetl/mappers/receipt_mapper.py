from iotexetl.utils import string_utils


def map_receipt(receipt):
    return {
        'status': receipt.status,
        'height': receipt.blkHeight,
        'hash': receipt.actHash.hex(),
        'gas_consumed': receipt.gasConsumed,
        'contract_address': receipt.contractAddress
    }