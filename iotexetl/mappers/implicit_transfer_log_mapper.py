from iotexetl.utils import string_utils


def map_implicit_transfer_log(raw):
    for action in raw.implicitTransferLog:
        for transaction in action.transactions:
            yield {
                'type': 'implicit_transfer_log',
                'action_hash': string_utils.base64_string(action.actionHash),
                'topic': string_utils.base64_string(transaction.topic),
                'amount': transaction.amount,
                'sender': transaction.sender,
                'recipient': transaction.recipient,
            }