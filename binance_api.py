import requests
from config import BINANCE_API_KEY

def get_binance_price(symbol):
    url = f'https://api.binance.com/api/v3/ticker/price?symbol={symbol}'
    response = requests.get(url)
    data = response.json()
    return float(data['price']) if 'price' in data else None