from binance_api import get_binance_price
from solana_api import get_sol_price
from arbitrage import find_arbitrage_opportunity
from config import tokens

for token in tokens:
    opportunity = find_arbitrage_opportunity(token)
    if opportunity:
        print(f'Arbitrage Opportunity: {opportunity}')