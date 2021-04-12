from brownie import accounts, network, Contract, LsLMSR, ConditionalTokens, FakeDai
import json
import requests

CT_address = '0xcC5440eFe983618018AB41b352da52853FD50ed3'
Dai_address = '0xD49DE638C0fBbA0b6c6b9Fda7D4469d06AF19C38'
Chainlink_reporter = '0xf89b107bD0b9642669A63e004Cf3E3c0AD59379E'

dai = Contract.from_abi('dai', address= Dai_address, abi=json.load(open('build/contracts/FakeDai.json','r'))['abi'])

with open('./config/accounts.json') as file:
    acc = json.load(file)
    api_key = acc['api-football']['api_key']

def parse_hex(s):
    t = hex(s).split('x')[-1]
    return t.zfill(2)

class Match:
    def __init__(self, gameweek, hometeam, awayteam):
        self.gameweek = [int(s) for s in gameweek.split() if s.isdigit()][0]
        self.hometeam = hometeam
        self.awayteam = awayteam

    def generate_matchid(self):
        return parse_hex(self.gameweek) + parse_hex(self.hometeam) + parse_hex(self.awayteam)

def get_teams():
    with open('./config/api_football_teams.json') as teams:
        return json.load(teams)

def get_account():
    return accounts.load('chainlink')

def mint(user, amount):
    dai.mint(user, amount * 1e18, {'from': accounts[0]})

def get_balance(user):
    return int(dai.balanceOf(user))

def get_upcoming_matches(teams):
    url = "https://api-football-v1.p.rapidapi.com/v3/fixtures"
    querystring = querystring = {"league":"39","season":"2020","next":"10"}
    headers = {
        'x-rapidapi-key': api_key,
        'x-rapidapi-host': "api-football-v1.p.rapidapi.com"
        }

    response = requests.request("GET", url, headers=headers, params=querystring).json()
    matches = []
    for fixture in response['response']:
        matches.append(Match(fixture['league']['round'], teams.index(fixture['teams']['home']['name']), teams.index(fixture['teams']['away']['name'])))
    return matches

def create_market(match, funding):
    match_id = match.generate_matchid()
    print('0x' + match_id.zfill(64), match_id)
    contract = LsLMSR.deploy(CT_address, Dai_address, {'from': accounts[0]})
    dai.approve(contract, funding*1e18, {'from': accounts[0]})
    contract.setup('0x1' + match_id.zfill(63), match_id, 3, funding*1e18, 500, {'from': accounts[0]})
    return contract

def main():
    user = get_account()
    balance = get_balance(user)
    teams = get_teams()
    matches = get_upcoming_matches(teams)
    network.gas_price(1e9)
    i = 0
    print('================')
    print('UPCOMING MATCHES')
    print('================')
    for match in matches:
        print('[%s]: %s vs %s' % (i, teams[match.hometeam], teams[match.awayteam]))
        i+=1
    print('Please select a match:')
    desired_match = int(input())

    if desired_match < 0 or desired_match > 9:
        raise "Invalid"

    print('')
    print('You have chosen: %s vs %s' % (teams[matches[desired_match].hometeam], teams[matches[desired_match].awayteam]))
    print('Your current balance is: $%.2f' % float(balance/1e18))

    print('How much will you fund the market with?')
    seed_funding = int(input())

    if seed_funding > balance:
        raise "You don't have enough money"

    # market = create_market(matches[desired_match], seed_funding)
    # print('Market deployed at %s' % market)

    matchx = Match('match week 31', 10, 1) #Liveprool vs aston villa
    market = create_market(matchx, seed_funding)
