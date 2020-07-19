from iotexetl.utils import string_utils


def map_evm_transfers(block_evm_transfers):
    for action in block_evm_transfers.actionEvmTransfers:
        for transfer in action.evmTransfers:
            yield {
                'type': 'evm_transfer',
                'height': block_evm_transfers.blockHeight,
                'action_hash': action.actionHash.hex(),
                'amount': string_utils.base64_string(transfer.amount),
                'from': getattr(transfer, 'from'),
                'to': transfer.to,
            }