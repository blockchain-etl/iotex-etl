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

import decimal
import json
import grpc

from iotexetl.rpc.iotexapi import api_pb2
from iotexetl.rpc.iotexapi import api_pb2_grpc

class IotexRpc:

    def __init__(self, provider_uri, timeout=60):
        self.timeout = timeout
        self.provider_uri = provider_uri
        # self.stub = api_pb2_grpc.APIServiceStub(grpc.insecure_channel(provider_uri))

    # def get(self, endpoint):
    #     raw_response = make_get_request(
    #         self.provider_uri + endpoint,
    #         timeout=self.timeout
    #     )
    #
    #     response = self._decode_rpc_response(raw_response)
    #     return response

    # def _decode_rpc_response(self, response):
    #     response_text = response.decode('utf-8')
    #     return json.loads(response_text, parse_float=decimal.Decimal)

    def get_block(self, block_id):
        with grpc.insecure_channel(self.provider_uri) as channel:
            stub = api_pb2_grpc.APIServiceStub(channel)
            return stub.GetRawBlocks(api_pb2.GetRawBlocksRequest(startHeight=block_id, count=1, withReceipts=True))
