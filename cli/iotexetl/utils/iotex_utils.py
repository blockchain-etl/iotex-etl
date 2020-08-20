import bech32
from eth_hash.auto import keccak as keccak_256

DEFAULT_ADDRESS_PREFIX = 'io'


def set_iotex_utils_context(address_prefix):
    global DEFAULT_ADDRESS_PREFIX
    DEFAULT_ADDRESS_PREFIX = address_prefix


def pubkey_to_address(pubkey, prefix=None):
    """This implements the algorithm described here https://github.com/iotexproject/iotex-address"""
    if prefix is None:
        prefix = DEFAULT_ADDRESS_PREFIX

    if pubkey is None or len(pubkey) < 1:
        return None
    pubkey_hash = keccak_256(pubkey[1:])
    if pubkey_hash is None or len(pubkey_hash) < 12:
        return None
    payload = pubkey_hash[12:]
    return bech32_encode(prefix, payload)


def pubkey_hex_to_address(pubkey_hex):
    if pubkey_hex is None:
        return None
    return pubkey_to_address(bytearray.fromhex(pubkey_hex))


def bech32_encode(hrp, witprog):
    five_bit_witprog = bech32.convertbits(witprog, 8, 5)
    if five_bit_witprog is None:
        return None
    ret = bech32.bech32_encode(hrp, five_bit_witprog)
    return ret
