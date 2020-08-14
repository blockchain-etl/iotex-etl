from iotexetl.utils import string_utils


def map_transaction_logs(raw_block, block_transaction_log):
    for log in block_transaction_log.transactionLogs.logs:
        for index, transaction in enumerate(log.transactions):
            yield {
                'type': 'transaction_log',
                'transaction_log_type': transaction.type,
                'height': block_transaction_log.blockIdentifier.height,
                'action_hash': log.actionHash.hex(),
                'index': index,
                'topic': string_utils.base64_string(transaction.topic),
                'amount': string_utils.to_int(transaction.amount),
                'sender': transaction.sender,
                'recipient': transaction.recipient,
                'timestamp': raw_block.block.header.core.timestamp.ToJsonString(),
            }