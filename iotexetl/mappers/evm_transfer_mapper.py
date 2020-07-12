from iotexetl.utils import string_utils


def map_evm_transfers(raw):
    for action in raw.actionEvmTransfers:
        for transfer in action.evmTransfers:
            yield {
                'type': 'evm_transfer',
                'height': raw.blockHeight,
                'action_hash': action.actionHash.hex(),
                'amount': string_utils.base64_string(transfer.amount),
                'from': getattr(transfer, 'from'),
                'to': transfer.to,
            }