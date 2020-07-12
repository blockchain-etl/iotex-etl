from iotexetl.utils import string_utils


def map_evm_transfers(raw):
    for action in raw.actionEvmTransfers:
        for transfer in action.evmTransfers:
            yield {
                'height': raw.blockHeight,
                'action_hash': string_utils.base64_string(action.actionHash),
                'amount': string_utils.base64_string(transfer.amount),
                'from': getattr(transfer, 'from'),
                'to': transfer.to,
            }