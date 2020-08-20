# MIT License
#
# Copyright (c) 2020 Evgeny Medvedev, evge.medvedev@gmail.com
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

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