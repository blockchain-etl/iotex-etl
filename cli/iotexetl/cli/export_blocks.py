# MIT License
#
# Copyright (c) 2020 Worawat Wijarn worawat.wijarn@gmail.com
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

import click

from iotexetl.jobs.export_blocks_job import ExportBlocksJob

from iotexetl.exporters.iotex_item_exporter import IotexItemExporter
from iotexetl.rpc.iotex_rpc import IotexRpc
from blockchainetl_common.logging_utils import logging_basic_config
from blockchainetl_common.thread_local_proxy import ThreadLocalProxy

from iotexetl.utils.iotex_utils import set_iotex_utils_context

logging_basic_config()


@click.command(context_settings=dict(help_option_names=['-h', '--help']))
@click.option('-s', '--start-block', default=0, show_default=True, type=int, help='Start block')
@click.option('-e', '--end-block', required=True, type=int, help='End block')
@click.option('-p', '--provider-uri', default='grpcs://api.mainnet.iotex.one:443', show_default=True, type=str,
              help='The URI of the remote IoTeX node.')
@click.option('-t', '--testnet', required=False, is_flag=True, help='Whether it\'s a testnet.')
@click.option('-w', '--max-workers', default=5, show_default=True, type=int, help='The maximum number of workers.')
@click.option('-b', '--batch-size', default=10, show_default=True, type=int,
              help='The number of blocks to export in batch.')
@click.option('-o', '--output-dir', default=None, type=str, help='The output directory for block data.')
@click.option('-f', '--output-format', default='json', show_default=True, type=click.Choice(['json']),
              help='The output format.')
def export_blocks(start_block, end_block, provider_uri, testnet, max_workers, batch_size, output_dir, output_format):
    """Exports blocks, actions, receipts, and logs."""

    if testnet:
        set_iotex_utils_context(address_prefix='it')

    job = ExportBlocksJob(
        start_block=start_block,
        end_block=end_block,
        iotex_rpc=ThreadLocalProxy(lambda: IotexRpc(provider_uri)),
        max_workers=max_workers,
        item_exporter=IotexItemExporter(output_dir, output_format=output_format),
        batch_size=batch_size
    )
    job.run()
