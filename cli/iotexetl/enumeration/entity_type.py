class EntityType:
    BLOCK = 'block'
    ACTION = 'action'
    LOG = 'log'
    EVM_TRANSFER = 'evm_transfer'
    TRANSACTION_LOG = 'transaction_log'

    ALL_FOR_STREAMING = [BLOCK, ACTION, LOG, TRANSACTION_LOG]
