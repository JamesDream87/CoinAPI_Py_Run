import requests
import json
from setting import config


con = config.config
url = 'https://rest.coinapi.io/v1/symbols?filter_symbol_id=BitStamp_SPOT_BTC_USD'
headers = {'X-CoinAPI-Key' : con['key']}
response = requests.get(url, headers=headers)

json_str = json.dumps(response.json())
# WriteData
fo = open("data.json", "w", encoding='utf-8')
fo.write(json_str)