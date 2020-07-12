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
import grpc


class IotexService(object):
    def __init__(self, iotex_rpc):
        self.iotex_rpc = iotex_rpc

    def get_genesis_block(self):
        return self.get_blocks(0)

    def get_latest_block(self):
        return self.get_blocks('head')

    def get_block(self, block_number):
        return self.get_blocks([block_number])

    def get_blocks(self, block_number_batch):
        if not block_number_batch:
            return []
        response = self.iotex_rpc.get_blocks(block_number_batch)
        return response.blocks

    def get_evm_transfers(self, block_number_batch):
        if not block_number_batch:
            return []
        for block_number in block_number_batch:
            try:
                response = self.iotex_rpc.get_evm_transfers(block_number)
                for evm_transfers in response.blockEvmTransfers:
                    yield evm_transfers
            except grpc.RpcError as e:
                if e.code() != grpc.StatusCode.NOT_FOUND:
                    print(e.details())
                    raise
