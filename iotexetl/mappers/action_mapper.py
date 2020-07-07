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
from iotexetl.utils import string_utils, iotex_utils


def map_action(response):
    for action in response.blocks[0].block.body.actions:
        action_dict = {}
        if action.core.WhichOneof('action') == 'transfer':
            action_dict = map_transfer(action)
        elif action.core.WhichOneof('action') == 'execution':
            action_dict = map_execution(action)
        elif action.core.WhichOneof('action') == 'startSubChain':
            action_dict = map_start_sub_chain(action)
        elif action.core.WhichOneof('action') == 'stopSubChain':
            action_dict = map_stop_sub_chain(action)
        elif action.core.WhichOneof('action') == 'putBlock':
            action_dict = map_put_block(action)
        elif action.core.WhichOneof('action') == 'createDeposit':
            action_dict = map_create_deposit(action)
        elif action.core.WhichOneof('action') == 'settleDeposit':
            action_dict = map_settle_deposit(action)
        elif action.core.WhichOneof('action') == 'createPlumChain':
            action_dict = map_create_plum_chain(action)
        elif action.core.WhichOneof('action') == 'terminatePlumChain':
            action_dict = map_terminate_plum_chain(action)
        elif action.core.WhichOneof('action') == 'plumPutBlock':
            action_dict = map_plum_put_block(action)
        elif action.core.WhichOneof('action') == 'plumCreateDeposit':
            action_dict = map_plum_create_deposit(action)
        elif action.core.WhichOneof('action') == 'plumStartExit':
            action_dict = map_plum_start_exit(action)
        elif action.core.WhichOneof('action') == 'plumChallengeExit':
            action_dict = map_plum_challenge_exit(action)
        elif action.core.WhichOneof('action') == 'plumResponseChallengeExit':
            action_dict = map_plum_response_challenge_exit(action)
        elif action.core.WhichOneof('action') == 'plumFinalizeExit':
            action_dict = map_plum_finalize_exit(action)
        elif action.core.WhichOneof('action') == 'plumSettleDeposit':
            action_dict = map_plum_settle_deposit(action)
        elif action.core.WhichOneof('action') == 'plumTransfer':
            action_dict = map_plum_transfer(action)
        elif action.core.WhichOneof('action') == 'depositToRewardingFund':
            action_dict = map_deposit_to_rewarding_fund(action)
        elif action.core.WhichOneof('action') == 'claimFromRewardingFund':
            action_dict = map_claim_from_rewarding_fund(action)
        elif action.core.WhichOneof('action') == 'grantReward':
            action_dict = map_grant_reward(action)
        elif action.core.WhichOneof('action') == 'stakeCreate':
            action_dict = map_stake_create(action)
        elif action.core.WhichOneof('action') == 'stakeUnstake':
            action_dict = map_stake_unstake(action)
        elif action.core.WhichOneof('action') == 'stakeWithdraw':
            action_dict = map_stake_withdraw(action)
        elif action.core.WhichOneof('action') == 'stakeAddDeposit':
            action_dict = map_stake_add_deposit(action)
        elif action.core.WhichOneof('action') == 'stakeRestake':
            action_dict = map_stake_restake(action)
        elif action.core.WhichOneof('action') == 'stakeChangeCandidate':
            action_dict = map_stake_change_candidate(action)
        elif action.core.WhichOneof('action') == 'stakeTransferOwnership':
            action_dict = map_stake_transfer_ownership(action)
        elif action.core.WhichOneof('action') == 'candidateRegister':
            action_dict = map_candidate_register(action)
        elif action.core.WhichOneof('action') == 'candidateUpdate':
            action_dict = map_candidate_update(action)
        elif action.core.WhichOneof('action') == 'putPollResult':
            action_dict = map_put_poll_result(action)

        yield {**map_base_action(action), **action_dict}

def map_base_action(action):
    return {
        'type': 'action',
        'version': action.core.version,
        'nonce': action.core.nonce,
        'gas_limit': action.core.gasLimit,
        'gas_price': action.core.gasPrice,
        'sender_pub_key': iotex_utils.pubkey_to_address(action.senderPubKey)
    }

def map_transfer(action):
    transfer = action.core.transfer
    return {
        'transfer': {
            'amount': transfer.amount,
            'recipient': transfer.recipient,
            'payload': string_utils.base64_string(transfer.payload),
        }
    }

def map_execution(action):
    execution = action.core.execution
    return {
        'execution': {
            'amount': execution.amount,
            'contract': execution.contract,
            'data': string_utils.base64_string(execution.data),
        }
    }

def map_start_sub_chain(action):
    start_sub_chain = action.core.startSubChain
    return {
        'start_sub_chain': {
            'chain_id': start_sub_chain.chainID,
            'security_deposit': start_sub_chain.securityDeposit,
            'operation_deposit': start_sub_chain.operationDeposit,
            'start_height': start_sub_chain.startHeight,
            'parent_height_offset': start_sub_chain.parentHeightOffset
        }
    }

def map_stop_sub_chain(action):
    stop_sub_chain = action.core.stopSubChain
    return {
        'stop_sub_chain': {
            'chain_id': stop_sub_chain.chainID,
            'stop_height': stop_sub_chain.stopHeight,
            'sub_chain_address': stop_sub_chain.subChainAddress
        }
    }

def map_put_block(action):
    put_block = action.core.putBlock
    return {
        'put_block': {
            'sub_chain_address': put_block.subChainAddress,
            'height': put_block.height,
            'roots': [{'name': root.name, 'value': string_utils.base64_string(root.value)} for root in put_block.roots]
        }
    }

def map_create_deposit(action):
    create_deposit = action.core.createDeposit
    return {
        'create_deposit': {
            'chain_id': create_deposit.chainID,
            'amount': create_deposit.amount,
            'recipient': create_deposit.recipient,
        }
    }

def map_settle_deposit(action):
    settle_deposit = action.core.settleDeposit
    return {
        'settle_deposit': {
            'amount': settle_deposit.amount,
            'recipient': settle_deposit.recipient,
            'index': settle_deposit.index
        }
    }

def map_create_plum_chain(action):
    return {}

def map_terminate_plum_chain(action):
    terminate_plum_chain = action.core.terminatePlumChain
    return {
        'terminate_plum_chain': {
            'sub_chain_address': terminate_plum_chain.subChainAddress
        }
    }

def map_plum_put_block(action):
    plum_put_block = action.core.plumPutBlock
    return {
        'plum_put_block': {
            'sub_chain_address': plum_put_block.subChainAddress,
            'height': plum_put_block.height,
            'roots': [{'name': name, 'value': string_utils.base64_string(value)} for name, value in plum_put_block.roots.items()],
        }
    }

def map_plum_create_deposit(action):
    plum_create_deposit = action.core.plumCreateDeposit
    return {
        'plum_create_deposit': {
            'sub_chain_address': plum_create_deposit.subChainAddress,
            'amount': plum_create_deposit.amount,
            'recipient': plum_create_deposit.recipient,
        }
    }

def map_plum_start_exit(action):
    plum_start_exit = action.core.plumStartExit
    return {
        'plum_start_exit': {
            'sub_chain_address': plum_start_exit.subChainAddress,
            'previous_transfer': string_utils.base64_string(plum_start_exit.previousTransfer),
            'previous_transfer_block_proof': string_utils.base64_string(plum_start_exit.previousTransferBlockProof),
            'previous_transfer_block_height': plum_start_exit.previousTransferBlockHeight,
            'exit_transfer': string_utils.base64_string(plum_start_exit.exitTransfer),
            'exit_transfer_block_proof': string_utils.base64_string(plum_start_exit.exitTransferBlockProof),
            'exit_transfer_block_height': plum_start_exit.exitTransferBlockHeight,
        }
    }

def map_plum_challenge_exit(action):
    plum_challenge_exit = action.core.plumChallengeExit
    return {
        'plum_challenge_exit': {
            'sub_chain_address': plum_challenge_exit.subChainAddress,
            'coin_id': plum_challenge_exit.coinID,
            'challenge_transfer': string_utils.base64_string(plum_challenge_exit.challengeTransfer),
            'challenge_transfer_block_proof': string_utils.base64_string(plum_challenge_exit.challengeTransferBlockProof),
            'challenge_transfer_block_height': plum_challenge_exit.challengeTransferBlockHeight,
        }
    }

def map_plum_response_challenge_exit(action):
    plum_response_challenge_exit = action.core.plumResponseChallengeExit
    return {
        'plum_response_challenge_exit': {
            'sub_chain_address': plum_response_challenge_exit.subChainAddress,
            'coin_id': plum_response_challenge_exit.coinID,
            'challenge_transfer': string_utils.base64_string(plum_response_challenge_exit.challengeTransfer),
            'response_transfer': string_utils.base64_string(plum_response_challenge_exit.responseTransfer),
            'response_transfer_block_proof': string_utils.base64_string(plum_response_challenge_exit.responseTransferBlockProof),
            'previous_transfer_block_height': plum_response_challenge_exit.previousTransferBlockHeight
        }
    }

def map_plum_finalize_exit(action):
    plum_finalize_exit = action.core.finalizeExit
    return {
        'plum_finalize_exit': {
            'sub_chain_address': plum_finalize_exit.subChainAddress,
            'coin_id': plum_finalize_exit.coinID,
        }
    }

def map_plum_settle_deposit(action):
    plum_settle_deposit = action.core.plumSettleDeposit
    return {
        'plum_settle_deposit': {
            'coin_id': plum_settle_deposit.coinID
        }
    }

def map_plum_transfer(action):
    plum_transfer = action.core.plumTransfer
    return {
        'plum_transfer': {
            'coin_id': plum_transfer.coinID,
            'denomination': string_utils.base64_string(plum_transfer.denomination),
            'owner': plum_transfer.owner,
            'recipient': plum_transfer.recipient,
        }
    }

def map_deposit_to_rewarding_fund(action):
    deposit_to_rewarding_fund = action.core.depositToRewardingFund
    return {
        'deposit_to_rewarding_fund': {
            'amount': deposit_to_rewarding_fund.amount,
            'data': string_utils.base64_string(deposit_to_rewarding_fund.data),
        }
    }

def map_claim_from_rewarding_fund(action):
    claim_from_rewarding_fund = action.core.claimFromRewardingFund
    return {
        'claim_from_rewarding_fund': {
            'amount': claim_from_rewarding_fund.amount,
            'data': string_utils.base64_string(claim_from_rewarding_fund.data),
        }
    }

def map_grant_reward(action):
    grant_reward = action.core.grantReward
    return {
        'grant_reward': {
            'type': grant_reward.type,
            'height': grant_reward.height
        }
    }

def map_stake_create(action):
    stake_create = action.core.stakeCreate
    return {
        'stake_create': {
            'candidate_name': stake_create.candidateName,
            'staked_amount': stake_create.stakedAmount,
            'staked_duration': stake_create.stakedDuration,
            'auto_stake': stake_create.autoStake,
            'payload': string_utils.base64_string(stake_create.payload),
        }
    }

def map_stake_unstake(action):
    stake_unstake = action.core.stakeUnstake
    return {
        'stake_unstake': {
            'bucket_index': stake_unstake.bucketIndex,
            'payload': string_utils.base64_string(stake_unstake.payload),
        }
    }

def map_stake_withdraw(action):
    stake_withdraw = action.core.stakeWithdraw
    return {
        'stake_withdraw': {
            'bucket_index': stake_withdraw.bucketIndex,
            'payload': string_utils.base64_string(stake_withdraw.payload),
        }
    }

def map_stake_add_deposit(action):
    stake_add_deposit = action.core.stakeAddDeposit
    return {
        'stake_add_deposit': {
            'bucket_index': stake_add_deposit.bucketIndex,
            'amount': stake_add_deposit.amount,
            'payload': string_utils.base64_string(stake_add_deposit.payload),
        }
    }

def map_stake_restake(action):
    stake_restake = action.core.stakeRestake
    return {
        'stake_restake': {
            'bucket_index': stake_restake.bucketIndex,
            'staked_duration': stake_restake.stakedDuration,
            'auto_stake': stake_restake.autoStake,
            'payload': string_utils.base64_string(stake_restake.payload),
        }
    }

def map_stake_change_candidate(action):
    stake_change_candidate = action.core.stakeChangeCandidate
    return {
        'stake_change_candidate': {
            'bucket_index': stake_change_candidate.bucketIndex,
            'candidate_name': stake_change_candidate.candidateName,
            'payload': string_utils.base64_string(stake_change_candidate.payload),
        }
    }

def map_stake_transfer_ownership(action):
    stake_transfer_ownership = action.core.stakeTransferOwnership
    return {
        'stake_transfer_ownership': {
            'bucket_index': stake_transfer_ownership.bucketIndex,
            'voter_address': stake_transfer_ownership.voterAddress,
            'payload': string_utils.base64_string(stake_transfer_ownership.payload),
        }
    }

def map_candidate_register(action):
    candidate_register = action.core.candidateRegister
    return {
        'candidate_register': {
            'name': candidate_register.candidate.name,
            'operator_address': candidate_register.candidate.operatorAddress,
            'reward_address': candidate_register.candidate.rewardAddress,
            'staked_amount': candidate_register.stakedAmount,
            'staked_duration': candidate_register.stakedDuration,
            'auto_stake': candidate_register.autoStake,
            'owner_address': candidate_register.ownerAddress,
            'payload': string_utils.base64_string(candidate_register.payload),
        }
    }

def map_candidate_update(action):
    candidate_update = action.core.candidateUpdate
    return {
        'candidate_update': {
            'name': candidate_update.name,
            'operator_address': candidate_update.operatorAddress,
            'reward_address': candidate_update.rewardAddress,
        }
    }

def map_put_poll_result(action):
    put_poll_result = action.core.putPollResult
    candidates = [map_candidate(candidate) for candidate in put_poll_result.candidates.candidates]
    return {
        'put_poll_result': {
            'height': put_poll_result.height,
            'candidates': candidates,
        }
    }

def map_candidate(candidate):
    return {
        'address': candidate.address,
        'votes': string_utils.base64_string(candidate.votes),
        'pub_key': string_utils.base64_string(candidate.pubKey),
        'reward_address': candidate.rewardAddress
    }