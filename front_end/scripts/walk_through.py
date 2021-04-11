from brownie import *

# this walk through script assumes that the contract has been deployed
# SUCCESS: A new account '0x55CeB36c28FbF1DAdf12B5d5006e2Bec5647FA4a' has been generated with the id 'chainlink_kovan'

factory_address = "???" # THIS IS MISSING MY BROTHER
user_address = "???" # what is the chainlink kovan thing? who is user here? 
question_id = "???"


lsLMSR = Contract.from_abi('lsLMSR', address= factory_address, abi=json.load(open('interfaces/lsLMSR.json','r')))

def get_account():
    return accounts.load('chainlink_kovan')

def get_contract():
    pass

def example_setup_market(question_id, oracle_address):
	print("Ser ... Setting up a market ")
	market_contract = lsLMSR.setup.call(
		oracle_address,
		question_id,
		3, # number of outcomes 
		1000, # subsidy
		300 #overround
		, {'from': user_address})
	return(market_contract)

def buy_outcome( outcome_id, amount):
	print("Buying outcome ser")
	lsLMSR.buy.call(outcome_id,amount,{'from': user_address})


def display_parameters(contract):
    pass




def main():
    user = get_account()
    contract = get_contract()
    display_parameters(contract)
    mkt = example_setup_market()
    

