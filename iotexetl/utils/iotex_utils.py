import bech32
from eth_hash.auto import keccak as keccak_256


def pubkey_to_address(pubkey_hex):
    """This implements the algorithm described here https://github.com/iotexproject/iotex-address"""
    if pubkey_hex is None or len(pubkey_hex) < 2:
        return None
    pubkey_hash = keccak_256(bytearray.fromhex(pubkey_hex[2:]))
    if pubkey_hash is None or len(pubkey_hash) < 12:
        return None
    payload = pubkey_hash[12:]
    return bech32_encode('io', payload)


def bech32_encode(hrp, witprog):
    five_bit_witprog = bech32.convertbits(witprog, 8, 5)
    if five_bit_witprog is None:
        return None
    ret = bech32.bech32_encode(hrp, five_bit_witprog)
    return ret
