from brownie import accounts, ChainlinkReporter

CT_address = '0xcC5440eFe983618018AB41b352da52853FD50ed3'

def get_account():
    return accounts.load('chainlink')

def main():
    user = get_account()
    ChainlinkReporter.deploy(CT_address, {'from': accounts[0]})
