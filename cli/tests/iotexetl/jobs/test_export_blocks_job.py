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

import pytest

from iotexetl.jobs.export_blocks_job import ExportBlocksJob
from iotexetl.exporters.iotex_item_exporter import IotexItemExporter
from tests.iotexetl.helpers import get_iotex_rpc
from blockchainetl_common.thread_local_proxy import ThreadLocalProxy

import tests.resources
from tests.helpers import compare_lines_ignore_order, read_file, skip_if_slow_tests_disabled

RESOURCE_GROUP = 'test_export_blocks_job'


def read_resource(resource_group, file_name):
    return tests.resources.read_resource([RESOURCE_GROUP, resource_group], file_name)


@pytest.mark.parametrize("start_block, end_block, resource_group ,provider_type", [
    (3290498, 3290498, 'blocks_with_actions', 'mock'),
    skip_if_slow_tests_disabled([3290498, 3290498, 'blocks_with_actions', 'online']),
    (5728441, 5728441, 'blocks_with_execution', 'mock'),
    skip_if_slow_tests_disabled([5728441, 5728441, 'blocks_with_execution', 'online']),
    (5914081, 5914081, 'blocks_with_put_poll_result', 'mock'),
    skip_if_slow_tests_disabled([5914081, 5914081, 'blocks_with_put_poll_result', 'online']),
    (5908046, 5908046, 'blocks_with_claim_from_rewarding_fund', 'mock'),
    skip_if_slow_tests_disabled([5908046, 5908046, 'blocks_with_claim_from_rewarding_fund', 'online']),
    (5911020, 5911020, 'blocks_with_stake_create', 'mock'),
    skip_if_slow_tests_disabled([5911020, 5911020, 'blocks_with_stake_create', 'online']),
])
def test_export_blocks_job(tmpdir, start_block, end_block, resource_group, provider_type):
    job = ExportBlocksJob(
        start_block=start_block,
        end_block=end_block,
        iotex_rpc=ThreadLocalProxy(
            lambda: get_iotex_rpc(
                provider_type,
                read_resource_lambda=lambda file: read_resource(resource_group, file))),
        max_workers=5,
        item_exporter=IotexItemExporter(str(tmpdir)),
    )
    job.run()

    all_files = ['blocks.json', 'actions.json', 'logs.json']

    for file in all_files:
        print(read_file(str(tmpdir.join(file))))
        compare_lines_ignore_order(
            read_resource(resource_group, f'expected_{file}'), read_file(str(tmpdir.join(file)))
        )
