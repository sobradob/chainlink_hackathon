from brownie import accounts

# SUCCESS: A new account '0x55CeB36c28FbF1DAdf12B5d5006e2Bec5647FA4a' has been generated with the id 'chainlink_kovan'

def get_account():
    return accounts.load('chainlink_kovan')

def get_contract():
    pass

def display_parameters(contract):
    pass


def main():
    user = get_account()
    contract = get_contract()
    display_parameters(contract)
