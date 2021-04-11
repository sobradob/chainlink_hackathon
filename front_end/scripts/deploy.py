from brownie import accounts, lsLMSR

# SUCCESS: A new account '0x55CeB36c28FbF1DAdf12B5d5006e2Bec5647FA4a' has been generated with the id 'chainlink_kovan'

def get_account():
    return accounts.load('chainlink_kovan')

def get_contract():
    pass

def display_parameters(contract):
    pass

def deploy_factory():
	factory_contract = lsLMSR.deploy({'from': accounts[0]})
	return factory_contract
	
def main():
    deploy_factory()

