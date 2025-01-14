import requests
from config import SOLANA_API_URL  # Make sure this is set to the correct base URL

def get_sol_price(token_pair):
    # Replace with the actual endpoint for the DEX you are using
    url = f'{SOLANA_API_URL}/v1/ticker/{token_pair}'  # Adjust based on actual API documentation
    response = requests.get(url)
    response.raise_for_status()  # Raise an error for bad responses
    data = response.json()
    return float(data['price']) if 'price' in data else None