# You Just Win
## Chainlink Hackathon Submission 2021


### Summary

We aim to produce a decentralised betting market that runs on the Ethereum blockchain and is secured by Chainlink.

For more important Chainlink related information please go to [you.just.win](you.just.win).

### Introduction

Online sports betting is a [$60bn dollar](https://www.statista.com/statistics/270728/market-volume-of-online-gaming-worldwide/) industry. This is a large market, and it has the potential to be even larger when one takes into account that sports betting is illegal under oppresive legislations in countries such as Cuba, China, North Korea, Somalia, Iran and the United States. 

Established players extract a significant amount of rent. Last year gambling executives scooped up [millions of dollars in bonuses and capital gains](https://www.thisismoney.co.uk/money/markets/article-9441845/UK-gambling-bosses-personal-wealth-increase-4-9bn.html). 

Just as Uniswap and other DEXs are disrupting the permissioned, centralised exchange model, gambling is ripe to be disrupted by open, decentralised exchanges. 


### Implementation

In order to design this project, three problems need to be addressed:

1. The oracle problem

The outcome of any event (such as "Who will win the 2020 US Presidential Election?") needs to be established and stored on the blockchain in a trust minimized manner.

2. Handling order book / market making

For the market to function, users need to be able to bet on certain outcomes.

3. Bootstrapping liquidity

In order to create competitive betting prices, the market must be sufficiently liquid.


## What makes our solution different

We decided to focus on what we see as the two main issues of existing implementations: 

- Liquidity providers have little incentive to create markets. For example, the [Omen FAQ](https://omen.eth.link/faq.pdf) points out that the liquidity providers can lose up to all funds by creating a market. The trading fees do not compensate for this risk.  
- The truth settlement mechanism is too complex. Using two different truth determining mechanisms (Realit.io and appeals with Kleros) or an additional token (REP) adds fees and unneccesary complexity.

We have chosen to solve this through: 

- Using an odds allocation algorithm that provides a bounded loss to the liquidity providers, ensuring they can never lose more than 10% of their initial liquidity. 
- Using overrounding to ensure that "the house always wins" and liquidity providers have considerable upside to providing liquidity. 
- Delegating the truth determining mechanism to Chainlink. 

### Implementation

In practice our implemention works the following way:

- An Initial Liquidity Provider (GAMEMASTER) creates a market on JUST WIN for a bet with at least two outcomes, setting the expiry date only. The liquidity they provide to the market can only be recovered after the bet has been settled.

- Users (BETTORS) make bets on multiple positions for the duration of the market. Essentially, bettors are purchasing futures contracts that expire at 1 if the outcome they bet on occurs, and 0 if it does not. The prices of these are set by the ODDS ALLOCATION ALGORITHM (OAA). The OAA is designed such that the GAMEMASTER will more often than not profit from the pool, although losses are still possible. The markets where a single outcome is guaranteed or extremely likely (Will I roll 1-6 with a dice?) are the most common types of market that make losses.


- Once the bet has expired, the Chainlink oracles  will report the outcome of the bet. The winners can claim their winnings and the GAMEMASTER recovers the initial liquidity pool and the additional profits. 


### Market Making & the Odds Allocation Algorithm

Orderbook based DEXes have not been widely adopted yet due to the high throughput they would require. In practical terms, orderbook based DEXes are highly inefficient in terms of gas. For this reason we'll use a fixed product automated market maker such as [Uniswap](https://app.uniswap.org/#/swap) to offer prices. 

There are many different algorithms available but we have chosen to use a modified LMSR ([logarithmic market scoring rule](https://www.cs.cmu.edu/~./sandholm/liquidity-sensitive%20automated%20market%20maker.teac.pdf)) to generate a fair price for any market.

The key advantage of this algorithm compared to that of Uniswap or Omen is that: 
- The losses to the GAMEMASTER are bounded (i.e. 80% drawdowns are simply not possible). 
- The algorithm uses overrounding to generate an expected profit for the GAMEMASTER. 

### Future Features

- Setting odds after a creating a market to maximize profit
- CashOut function for users to sell back their bets to the market.
- Allow others to add liquidity to a bet, not just the GAMEMASTER. 
