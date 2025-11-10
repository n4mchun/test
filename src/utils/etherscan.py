import requests
import os

TOKEN_TX_ACTION = 'tokentx'
TX_LIST_ACTION = 'txlist'

API_URL = 'https://api.etherscan.io/v2/api'
API_KEY = os.getenv('ETHERSCAN_API_KEY')

def fetch_account_api(address: str, chain_id: int, action: str) -> list:
    params = {
        'chainid': chain_id,
        'module': 'account',
        'action': action,
        'address': address,
        'apikey': API_KEY
    }

    response = requests.get(API_URL, params=params)
    response.raise_for_status()

    data = response.json()
    result = data.get('result', [])
    return result