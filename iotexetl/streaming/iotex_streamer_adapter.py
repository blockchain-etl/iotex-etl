import logging

from blockchainetl_common.jobs.exporters.console_item_exporter import ConsoleItemExporter
from blockchainetl_common.jobs.exporters.in_memory_item_exporter import InMemoryItemExporter
from iotexetl.enumeration.entity_type import EntityType
from iotexetl.jobs.export_blocks_job import ExportBlocksJob

from iotexetl.jobs.export_evm_transfers_job import ExportEvmTransfersJob


class IotexStreamerAdapter:
    def __init__(
            self,
            iotex_rpc,
            item_exporter=ConsoleItemExporter(),
            batch_size=100,
            max_workers=5,
            entity_types=tuple(EntityType.ALL_FOR_STREAMING)):
        self.iotex_rpc = iotex_rpc
        self.item_exporter = item_exporter
        self.batch_size = batch_size
        self.max_workers = max_workers
        self.entity_types = entity_types

    def open(self):
        self.item_exporter.open()

    def get_current_block_number(self):
        meta = self.iotex_rpc.get_chain_meta()
        return meta.chainMeta.height

    def export_all(self, start_block, end_block):
        # Export blocks, actions and logs
        blocks, actions, logs = [], [], []
        if self._should_export(EntityType.BLOCK) or self._should_export(EntityType.ACTION) or self._should_export(EntityType.LOG):
            blocks, transactions, logs = self._export_blocks(start_block, end_block)

        # Extract evm transfers
        evm_transfers = []
        if self._should_export(EntityType.EVM_TRANSFER):
            evm_transfers = self._export_evm_transfers(start_block, end_block)

        enriched_blocks = blocks if EntityType.BLOCK in self.entity_types else []
        enriched_actions = actions if EntityType.ACTION in self.entity_types else []
        enriched_logs = logs if EntityType.LOG in self.entity_types else []
        enriched_evm_transfers = evm_transfers if EntityType.EVM_TRANSFER in self.entity_types else []

        logging.info('Exporting with ' + type(self.item_exporter).__name__)

        all_items = enriched_blocks + \
            enriched_actions + \
            enriched_logs + \
            enriched_evm_transfers

        self.item_exporter.export_items(all_items)

    def _export_blocks(self, start_block, end_block):
        item_exporter = InMemoryItemExporter(item_types=[EntityType.BLOCK, EntityType.ACTION, EntityType.LOG])
        job = ExportBlocksJob(
            start_block=start_block,
            end_block=end_block,
            batch_size=self.batch_size,
            iotex_rpc=self.iotex_rpc,
            max_workers=self.max_workers,
            item_exporter=item_exporter,
            export_blocks=self._should_export(EntityType.BLOCK),
            export_actions=self._should_export(EntityType.ACTION),
            export_logs=self._should_export(EntityType.LOG),
        )
        job.run()
        blocks = item_exporter.get_items(EntityType.BLOCK)
        actions = item_exporter.get_items(EntityType.ACTION)
        logs = item_exporter.get_items(EntityType.LOG)
        return blocks, actions, logs

    def _export_evm_transfers(self, start_block, end_block):
        item_exporter = InMemoryItemExporter(item_types=[EntityType.EVM_TRANSFER])
        job = ExportEvmTransfersJob(
            start_block=start_block,
            end_block=end_block,
            iotex_rpc=self.iotex_rpc,
            max_workers=self.max_workers,
            item_exporter=item_exporter)
        job.run()
        evm_transfers = item_exporter.get_items(EntityType.EVM_TRANSFER)
        return evm_transfers

    def _should_export(self, entity_type):
        if entity_type == EntityType.BLOCK:
            return True

        if entity_type == EntityType.ACTION \
                or entity_type == EntityType.LOG \
                or entity_type == EntityType.EVM_TRANSFER:
            return entity_type in self.entity_types

        raise ValueError('Unexpected entity type ' + entity_type)

    def close(self):
        self.item_exporter.close()