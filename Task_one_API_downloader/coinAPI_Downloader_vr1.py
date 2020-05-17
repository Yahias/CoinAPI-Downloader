"""
This Script is for fetching the historical data from cryptocurrencies from CoinAPI.io since the January 1st of 2016.
List of cryptocurrencies: [Bitcoin (BTC), Ethereum (ETH), Ripple (XRP),Litecoin (LTC) ]

Input variables: 
    - cryptocurrency code example : Bitcoin --> BTC
    - API Key
Output format:
    - Json file with the result, named as result_start_date - end_date.json
"""

import os
import requests
import pandas as pd
from io import StringIO
from datetime import datetime
import argparse
import json



parser = argparse.ArgumentParser()
parser.add_argument("-c", "--currencysymbol", required=True,help="Currencty Symbol for example BTC,ETH,XRP,LTC")
parser.add_argument("-k", "--key", required=True,help="Your API KEY")
args = parser.parse_args()

currency_code=args.currencysymbol
#currency_code='btc'
#API_KEY ='3D68E0FD-95B6-4673-945B-83A5967955B6'
API_KEY =args.key
headers = {'X-CoinAPI-Key': API_KEY}
#start_date='2016-01-01T00:00:00'
start_date='2016-06-06'
end_date=datetime.today().replace(microsecond=0).isoformat()
period = '1DAY'
limit = '10000'
asset_id_base=currency_code.upper()
asset_id_quote='USD'

print(f'Starting of fetching historical data of {currency_code}')

url = f'https://rest.coinapi.io/v1/ohlcv/{asset_id_base}/{asset_id_quote}/history?period_id={period}&time_start={start_date}&time_end={end_date}&limit={limit}'



resp = requests.get(url,headers=headers)
result_json=resp.json()
print(result_json)
with open(f'result_{start_date} - {end_date}.json', 'w') as outfile:
    json.dump(result_json, outfile)












