class EntityType:
    BLOCK = 'block'
    ACTION = 'action'
    LOG = 'log'
    EVM_TRANSFER = 'evm_transfer'

    ALL_FOR_STREAMING = [BLOCK, ACTION, LOG, EVM_TRANSFER]
