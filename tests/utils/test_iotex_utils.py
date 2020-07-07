import pytest

from iotexetl.utils.iotex_utils import pubkey_to_address


@pytest.mark.parametrize("pubkey,expected_address", [
    ['04e93b5b1c8fba69263652a483ad55318e4eed5b5122314cb7fdb077d8c7295097cec92ee50b1108dc7495a9720e5921e56d3048e37abe6a6716d7c9b913e9f2e6', 'io1juvx5g063eu4ts832nukp4vgcwk2gnc5cu9ayd'],
    ['04bc3a3123a0d72e1e622ec1a51087ef3b15a9d6db0f924c0fd8b4958653ff7608194321d1fd90c0c949b05b6b911d8d7e9aaadbe497e696367c19780a016ce440', 'io1llupp3n8q5x8usnr5w08j6hc6hn55x64l46rr7'],

])
def test_pubkey_to_address(pubkey, expected_address):
    address = pubkey_to_address(pubkey)
    assert address == expected_address