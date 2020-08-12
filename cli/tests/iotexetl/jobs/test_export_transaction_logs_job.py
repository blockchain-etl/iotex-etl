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

from iotexetl.jobs.export_transaction_logs_job import ExportTransactionLogsJob
from iotexetl.exporters.iotex_item_exporter import IotexItemExporter
from tests.iotexetl.helpers import get_iotex_rpc
from blockchainetl_common.thread_local_proxy import ThreadLocalProxy

import tests.resources
from tests.helpers import compare_lines_ignore_order, read_file, skip_if_slow_tests_disabled

RESOURCE_GROUP = 'test_export_transaction_logs_job'


def read_resource(resource_group, file_name):
    return tests.resources.read_resource([RESOURCE_GROUP, resource_group], file_name)


@pytest.mark.parametrize("start_block, end_block, resource_group ,provider_type", [
    (5202793, 5202793, 'transaction_logs', 'mock'),
    skip_if_slow_tests_disabled([5202793, 5202793, 'transaction_logs', 'online']),
])
def test_export_transaction_logs_job(tmpdir, start_block, end_block, resource_group, provider_type):
    job = ExportTransactionLogsJob(
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

    compare_lines_ignore_order(
        read_resource(resource_group, 'expected_transaction_logs.json'), read_file(str(tmpdir.join('transaction_logs.json')))
    )