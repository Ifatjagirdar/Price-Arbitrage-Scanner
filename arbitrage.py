from binance_api import get_binance_price
from solana_api import get_sol_price
from utils import calculate_net_price

SLIPPAGE = 0.01  # 1% slippage

def find_arbitrage_opportunity(token_pair):
    binance_symbol = f'{token_pair}USDC'
    solana_symbol = f'{token_pair}-USDC'  # Adjust based on DEX API

    binance_price = get_binance_price(binance_symbol)
    solana_price = get_sol_price(solana_symbol)

    if binance_price is None or solana_price is None:
        return None

    net_binance_price = calculate_net_price(binance_price, BINANCE_FEE)
    net_sol_price = calculate_net_price(solana_price, SOLANA_FEE + TRANSACTION_COST)

    # Adjust for slippage
    expected_profit = net_sol_price - net_binance_price
    adjusted_profit = expected_profit * (1 - SLIPPAGE)

    if adjusted_profit > 0:
        return {
            'token_pair': token_pair,
            'binance_price': net_binance_price,
            'solana_price': net_sol_price,
            'profit': adjusted_profit
        }
    return None