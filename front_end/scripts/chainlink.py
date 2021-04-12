from brownie import accounts, network, Contract, LsLMSR
import json

# put the address of LSLMSR here
chainlink_address = '0xD95e3d8F095E52be7f8eB35F44aE9595834004AF'
link = Contract.from_abi('link', address= chainlink_address, abi=json.load(open('build/contracts/LsLMSR.json','r'))['abi'])

def get_account():
    return accounts.load('chainlink')

def main():
    user = get_account()
    network.gas_price(1e9)
    network.gas_limit(1000000)
    link.requestMatchOutcome({'from': accounts[0], 'allow_revert': True})
