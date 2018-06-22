#! python3

import json
from bittrex.bittrex import Bittrex, API_V2_0

amount = 0
price = 0

with open('D:/code/emailtrade/keys.json') as k:
    keys = json.load(k)
api_key = keys['api_key']
priv_key = keys['priv_key']


trex = Bittrex(api_key, priv_key, api_version=API_V2_0)
def marketcheck(ticker):
    markets = trex.get_ticker(ticker)
    price = markets['result']['Ask']
    print(markets['result'])
    print(price)
    return price

marketcheck('BTC-LTC')


#def open_buy():
   # trex.buy_limit(ticker, amount, price)