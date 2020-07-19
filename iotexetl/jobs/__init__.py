from grpc import RpcError
from requests.exceptions import Timeout as RequestsTimeout, HTTPError, TooManyRedirects
from blockchainetl_common.executors.retriable_value_error import RetriableValueError

RETRY_EXCEPTIONS = (
    ConnectionError, HTTPError, RequestsTimeout, TooManyRedirects, OSError, RetriableValueError,
    RpcError)
