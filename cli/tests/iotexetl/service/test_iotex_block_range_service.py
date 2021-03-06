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
from dateutil.parser import parse

from iotexetl.service.iotex_block_range_service import IotexBlockRangeService
from blockchainetl_common.graph.graph_operations import OutOfBoundsError
from tests.iotexetl.helpers import get_iotex_rpc
from tests.helpers import skip_if_slow_tests_disabled


@pytest.mark.parametrize("date,expected_start_block,expected_end_block", [
    skip_if_slow_tests_disabled(['2019-04-22', 1, 7828]),
    skip_if_slow_tests_disabled(['2020-07-15', 5908040, 5925317]),
])
def test_get_block_range_for_date(date, expected_start_block, expected_end_block):
    iotex_block_range_service = get_iotex_block_range_service()
    parsed_date = parse(date)
    blocks = iotex_block_range_service.get_block_range_for_date(parsed_date)
    assert (expected_start_block, expected_end_block) == blocks


@pytest.mark.parametrize("date", [
    skip_if_slow_tests_disabled(['2019-01-01'])
])
def test_get_block_range_for_date_fail(date):
    iotex_block_range_service = get_iotex_block_range_service()
    parsed_date = parse(date)
    with pytest.raises(OutOfBoundsError):
        iotex_block_range_service.get_block_range_for_date(parsed_date)


def get_iotex_block_range_service():
    return IotexBlockRangeService(get_iotex_rpc("online"))
