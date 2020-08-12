# The MIT License (MIT)
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
from urllib.parse import urlparse

import grpc

from iotexetl.rpc.iotexapi import api_pb2
from iotexetl.rpc.iotexapi import api_pb2_grpc


class IotexRpc:

    def __init__(self, provider_uri, timeout=60):
        self.timeout = timeout
        channel = get_channel_from_uri_string(provider_uri)
        self.stub = api_pb2_grpc.APIServiceStub(channel)

    def get_raw_blocks(self, start_height, count):
        return self.stub.GetRawBlocks(
            api_pb2.GetRawBlocksRequest(startHeight=start_height, count=count, withReceipts=True), timeout=self.timeout)

    def get_block_metas(self, start_height, count):
        return self.stub.GetBlockMetas(api_pb2.GetBlockMetasRequest(
            byIndex=api_pb2.GetBlockMetasByIndexRequest(start=start_height, count=count)
        ), timeout=self.timeout)

    def get_transaction_logs(self, block_number):
        return self.stub.GetTransactionLogByBlockHeight(
            api_pb2.GetTransactionLogByBlockHeightRequest(blockHeight=block_number), timeout=self.timeout)

    def get_logs(self, block_number_batch):
        return self.stub.GetLogs(api_pb2.GetLogsRequest(filter=api_pb2.LogsFilter(),
                                                        byRange=api_pb2.GetLogsByRange(fromBlock=block_number_batch[0],
                                                                                       count=len(block_number_batch))),
                                 timeout=self.timeout)

    def get_chain_meta(self):
        return self.stub.GetChainMeta(api_pb2.GetChainMetaRequest(), timeout=self.timeout)


def get_channel_from_uri_string(provider_uri):
    uri = urlparse(provider_uri)
    if uri.scheme == 'grpcs':
        credentials = grpc.ssl_channel_credentials()
        channel = grpc.secure_channel(uri.netloc, credentials)
    elif uri.scheme == 'grpc':
        channel = grpc.insecure_channel(uri.netloc)
    else:
        raise ValueError(f'The uri scheme {uri.scheme} is not recognized. Use grpc:// or grpcs://')

    return channel
