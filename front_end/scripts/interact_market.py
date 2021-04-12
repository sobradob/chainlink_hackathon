from brownie import accounts, Contract, LsLMSR
import json

market_address = '0xe576aD1383CB3eA15132773Da6061602fD8649Cb'
market = Contract.from_abi('market', address= market_address, abi=json.load(open('build/contracts/LsLMSR.json','r'))['abi'])

# old market = 0xCeC4B896955F5EFC9E981974b030c7D862DD7dEB

outcomes = ['HOME WIN', 'DRAW', 'AWAY WIN']

Dai_address = '0xD49DE638C0fBbA0b6c6b9Fda7D4469d06AF19C38'
dai = Contract.from_abi('dai', address= Dai_address, abi=json.load(open('build/contracts/FakeDai.json','r'))['abi'])

CT_address = '0xcC5440eFe983618018AB41b352da52853FD50ed3'
ct = Contract.from_abi('ct', address= CT_address, abi=json.load(open('build/contracts/ConditionalTokens.json','r'))['abi'])


def get_account():
    return accounts.load('chainlink')

def get_contract():
    pass

def display_parameters(contract):
    print('The contract is currently funded with $%.2f' % float(contract.cost()/(2**64)))
    for i in [0,1,2]:
        print('The price for outcome %s is $%.2f' % (outcomes[i], float(contract.price(2**i,(2**64))/(2**64))))
    outcome = contract.outcome()
    print('Outcome is %s' % outcome)

def buy_tokens(option, amount):
    dai.approve(market, amount*1e18, {'from': accounts[0]})
    market.buy(2**option, amount*(2**64), {'from': accounts[0]})


def main():
    user = get_account()
    display_parameters(market)
    allowed_outcomes = ['H', 'D', 'A']
    print('Which outcome do you want to buy?')
    print('[H]: HOME WIN')
    print('[D]: DRAW')
    print('[A]: AWAY WIN')
    option = input()

    if option not in allowed_outcomes:
        raise 'Invalid option'

    print('How many outcome tokens do you want to buy?')

    tokens = int(input())

    buy_tokens(allowed_outcomes.index(option), tokens)

    display_parameters(market)
