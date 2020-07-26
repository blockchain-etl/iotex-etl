from iotexetl.utils.string_utils import to_int


def map_receipt(receipt):
    return {
        'status': receipt.status,
        'height': receipt.blkHeight,
        'hash': receipt.actHash.hex(),
        'gas_consumed': to_int(receipt.gasConsumed),
        'contract_address': receipt.contractAddress
    }