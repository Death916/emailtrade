import json
from bittrex import Bittrex
import history as hist


price = 0

with open('D:/code/emailtrade/keys.json') as k:
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
    buy_amount = .0005 / buyprice
    # print(trex.buy_limit(ticker, amount, rate=buyprice))
    print('buying',  buy_amount, 'of', ticker)
    hist.tradehist('bought ' + str(buy_amount) + ' of ' + ticker + ' at ' + str(buyprice))
    return

def close_trade():
    global sellprice
    sellprice = marketcheck(ticker)
    amount = .0005 / sellprice
    # print(trex.sell_limit(ticker, amount, rate=sellprice))
    print('selling',  amount, 'of', ticker)
    hist.tradehist('sold ' + str(amount) + ' of ' + ticker + ' at ' + str(sellprice))
    global buy_amount
    hist.tradehist('profit = ' + '{:.25f}'.format((sellprice * amount) - (buyprice * amount)))

def open_orders():
    trex.get_open_orders()
    return

