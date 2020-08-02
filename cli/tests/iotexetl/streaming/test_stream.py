# MIT License
#
# Copyright (c) 2018 Evgeny Medvedev, evge.medvedev@gmail.com
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

import os

import pytest
from blockchainetl_common.thread_local_proxy import ThreadLocalProxy

from iotexetl.streaming.iotex_streamer_adapter import IotexStreamerAdapter

import tests.resources
from iotexetl.enumeration.entity_type import EntityType
from blockchainetl_common.jobs.exporters.composite_item_exporter import CompositeItemExporter
from blockchainetl_common.streaming.streamer import Streamer
from tests.helpers import compare_lines_ignore_order, read_file, skip_if_slow_tests_disabled
from tests.iotexetl.helpers import get_iotex_rpc

RESOURCE_GROUP = 'test_stream'


def read_resource(resource_group, file_name):
    return tests.resources.read_resource([RESOURCE_GROUP, resource_group], file_name)


@pytest.mark.parametrize("start_block, end_block, batch_size, resource_group, entity_types, provider_type", [
    (5890945, 5890945, 1, 'blocks_with_actions', ['block', 'action', 'log'], 'mock'),
    (5892481, 5892481, 1, 'blocks_with_put_poll_result', ['block', 'action', 'log'], 'mock'),
    (5890899, 5890899, 1, 'blocks_with_claim_from_rewarding_fund', ['block', 'action', 'log'], 'mock'),
    (5892110, 5892110, 1, 'blocks_with_stake_create', ['block', 'action', 'log'], 'mock'),
    (5906248, 5906248, 1, 'evm_transfers', ['evm_transfer'], 'mock'),
])
def test_stream(tmpdir, start_block, end_block, batch_size, resource_group, entity_types, provider_type):
    try:
        os.remove('last_synced_block.txt')
    except OSError:
        pass

    blocks_output_file = str(tmpdir.join('actual_blocks.json'))
    actions_output_file = str(tmpdir.join('actual_actions.json'))
    logs_output_file = str(tmpdir.join('actual_logs.json'))
    evm_transfers_output_file = str(tmpdir.join('actual_evm_transfers.json'))

    streamer_adapter = IotexStreamerAdapter(
        iotex_rpc=ThreadLocalProxy(
            lambda: get_iotex_rpc(
                provider_type,
                read_resource_lambda=lambda file: read_resource(resource_group, file))),
        batch_size=batch_size,
        item_exporter=CompositeItemExporter(
            filename_mapping={
                'block': blocks_output_file,
                'action': actions_output_file,
                'log': logs_output_file,
                'evm_transfer': evm_transfers_output_file,
            }
        ),
        entity_types=entity_types,
    )
    streamer = Streamer(
        blockchain_streamer_adapter=streamer_adapter,
        start_block=start_block,
        end_block=end_block,
        retry_errors=False
    )
    streamer.stream()

    if EntityType.BLOCK in entity_types:
        print('=====================')
        print(read_file(blocks_output_file))
        compare_lines_ignore_order(
            read_resource(resource_group, 'expected_blocks.json'), read_file(blocks_output_file)
        )

    if EntityType.ACTION in entity_types:
        print('=====================')
        print(read_file(actions_output_file))
        compare_lines_ignore_order(
            read_resource(resource_group, 'expected_actions.json'), read_file(actions_output_file)
        )

    if EntityType.LOG in entity_types:
        print('=====================')
        print(read_file(logs_output_file))
        compare_lines_ignore_order(
            read_resource(resource_group, 'expected_logs.json'), read_file(logs_output_file)
        )

    if EntityType.EVM_TRANSFER in entity_types:
        print('=====================')
        print(read_file(evm_transfers_output_file))
        compare_lines_ignore_order(
            read_resource(resource_group, 'expected_evm_transfers.json'), read_file(evm_transfers_output_file)
        )
