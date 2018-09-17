import json
from bittrex import Bittrex
import history as hist
import os

price = 0

with open(os.getcwd() + '/keys.json') as k:
    keys = json.load(k)
    
api_key = keys['api_key']
priv_key = keys['priv_key']
ticker = 'BTC-ETH'
trex = Bittrex(api_key, priv_key)


def marketcheck(ticker):
    markets = trex.get_ticker(ticker)               
    price = markets['result']['Ask']
    print(ticker, 'price is ', price)
    return price


def open_trade():
    global buyprice
    buyprice = marketcheck(ticker)
    global buy_amount
    balance = trex.get_balance('BTC')['result']['Available']
    buy_amount = balance / buyprice
    # print(trex.buy_limit(ticker, amount, rate=buyprice))
    print('buying',  buy_amount, 'of', ticker)
    hist.tradehist('bought ' + str(buy_amount) + ' of ' + ticker + ' at ' + str(buyprice))
    return

def close_trade():
    global sellprice
    sellprice = marketcheck(ticker)
    global buy_amount
    sell_amount =  buy_amount
    #sell_amount = trex.get_balance('ETH')['result']['Available']
    # print(trex.sell_limit(ticker, amount, rate=sellprice))
    print('selling',  sell_amount, 'of', ticker)
    hist.tradehist('sold ' + str(sell_amount) + ' of ' + ticker + ' at ' + str(sellprice))
    hist.tradehist('profit = ' + '{:.25f}'.format((sellprice * sell_amount) - (buyprice * sell_amount)))

def open_orders():
    trex.get_open_orders()
    return

