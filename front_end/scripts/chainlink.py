from brownie import accounts, network, Contract, LsLMSR
import json

chainlink_address = '0xe576aD1383CB3eA15132773Da6061602fD8649Cb'
link = Contract.from_abi('link', address= chainlink_address, abi=json.load(open('build/contracts/LsLMSR.json','r'))['abi'])

def get_account():
    return accounts.load('chainlink')

def main():
    user = get_account()
    network.gas_price(1e9)
    network.gas_limit(1000000)
    link.requestMatchOutcome({'from': accounts[0], 'allow_revert': True})
