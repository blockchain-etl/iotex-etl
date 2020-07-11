from iotexetl.utils import string_utils


def map_receipt(receipt):
    return {
        'status': receipt.status,
        'height': receipt.blkHeight,
        'hash': string_utils.base64_string(receipt.actHash),
        'gas_consumed': receipt.gasConsumed,
        'contract_address': receipt.contractAddress
    }