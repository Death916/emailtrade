#! python3

import json
from bittrex.bittrex import Bittrex, API_V2_0 
from bittrex import Bittrex as trex1
import history as hist

amount = 0
price = 0

with open('D:/code/emailtrade/keys.json') as k:
    keys = json.load(k)
    
api_key = keys['api_key']
priv_key = keys['priv_key']
ticker = 'BTC-ETH'
trex = Bittrex(api_key, priv_key, api_version=API_V2_0)


def marketcheck(ticker):
    markets = trex.get_latest_candle(ticker, 'fiveMin')
    #price = markets['result']['Ask']
    print(markets)
    return price


def open_trade(amount):
    global buyprice
    buyprice = marketcheck(ticker)
    trex.buy_limit(ticker, amount, rate = buyprice)
    print('buying',  amount, 'of', ticker)
    hist.tradehist('bought ' +  amount + ' of ' + ticker + ' at ' + str(buyprice))
    print(buyprice)

def close_trade(amount):
    global sellprice
    sellprice = marketcheck(ticker)
    trex.sell_limit(ticker, amount, rate = None)
    print('selling',  amount, 'of', ticker)
    hist.tradehist('sold ' +  amount + ' of ' + ticker + ' at ' + str(sellprice))
    hist.tradehist('profit = ' + str(sellprice - buyprice))

def open_orders():
    trex.get_open_orders()

    

#open_trade('.00051')
#close_trade('1')
marketcheck(ticker)
