class EntityType:
    BLOCK = 'block'
    ACTION = 'action'
    LOG = 'log'
    TRANSACTION_LOG = 'transaction_log'

    ALL_FOR_STREAMING = [BLOCK, ACTION, LOG, TRANSACTION_LOG]
