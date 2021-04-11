from brownie import *

# this walk through script assumes that the contract has been deployed
# SUCCESS: A new account '0x55CeB36c28FbF1DAdf12B5d5006e2Bec5647FA4a' has been generated with the id 'chainlink_kovan'

factory_address = "???" # THIS IS MISSING MY BROTHER
user_address = "???" # what is the chainlink kovan thing? who is user here? 
question_id = "???"


# deployed_lsLMSR = Contract.from_abi('lsLMSR', address= factory_address, abi=json.load(open('interfaces/lsLMSR.json','r')))

def get_account():
    return accounts.load('chainlink_kovan')

def get_contract():
	factory_contract = lsLMSR.deploy({'from': accounts[0]})
    return(factory_contract)

def get_price(lsmr_contract,outcome, amount):
	current_price = lsmr_contract.price.call(outcome, amount {'from': accounts[0]})
	return(current_price)
	### probably to do: set up function to make it human legible and nice

def setup_market(lsmr_contract, question_id, oracle_address, subsidy, overround):
	print("Ser ... Setting up a market ")
	print("Setting up market {} with the subsidy of {} and overround parameters of {} bps".format(question_id, subsidy,overround))
	market_contract = lsmr_contract.setup.call(
		oracle_address,
		question_id,
		3, # number of outcomes 
		subsidy, 
		overround #overround
		, {'from': user_address})
	return(market_contract)

def buy_outcome(lsmr_contract,outcome_id, amount):
	print("Buying outcome ser")
	lsmr_contract.buy.call(outcome_id,amount,{'from': user_address})


def display_parameters(contract):
    pass




def main():
    user = get_account()
    lsmr_contract = get_contract()
    display_parameters(lsmr_contract)
    ## start market set up 
    mkt = setup_market(lsmr_contract, 1, ??oracle_address, 100000, 300)


