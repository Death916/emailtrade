import json

import history as hist
import os
import krakenex
from pykrakenapi import KrakenAPI
import pandas as pd

price = 0

with open(os.getcwd() + "/keys.json") as k:
    keys = json.load(k)

API_KEY = keys["public"]
PRIV_KEY = keys["priv"]
TICKER= "ETHUSD"
API  = krakenex.API(API_KEY,  PRIV_KEY)
TIME = ""
EXCHANGE = "kraken"
PRICE = ""
PROFIT = ""
#BUY_CURRENCY = input().capitalize()

kraken = KrakenAPI(API)



def marketcheck(TICKER):
    markets =  kraken.get_ohlc_data(TICKER)
    price = markets[0]['close'][0]
    print(TICKER, "price is ", price)
    return price


#done

def open_trade():
    pd.options.display.float_format = '{:.2f}'.format
    global buyprice
    buyprice = marketcheck(TICKER)
    balancedf = kraken.get_account_balance() 
    balance = balancedf.vol["ZUSD"]
    global buy_amount
    buy_amount = (balance / buyprice) - (balance / buyprice) * 0.0025
    # kraken.add_standard_order(TICKER,)
    print("buying", buy_amount, "of", TICKER)
    hist.tradehist(
        "bought " + str(buy_amount) + " of " + TICKER+ " at " + str(buyprice)
    )
    return


def close_trade():

    sell_price = marketcheck(TICKER)
    if TICKER == 'ETHUSD':
        symbol = 'XETH'
    if TICKER == 'XBTUSD':
        symbol ='XXBT'


    balance = kraken.get_account_balance()
    sell_amount = buy_amount
    #sell_amount = balance.vol[symbol]
   # print(trex.sell_limit(TICKER, sell_amount, rate=sellprice))
    print("selling", sell_amount, "of", TICKER)
    hist.tradehist(
        "sold " + str(sell_amount) + " of " + TICKER+ " at " + str(sell_price)
    )
    """hist.tradehist(
        "profit = "
        + "{:.25f}".format((sell_price * sell_amount) - (buyprice * sell_amount)))
    """
    profit = (sell_price * sell_amount) - (buyprice * sell_amount)
    hist.tradehist("profit = " + "{:.25}".format(profit))

def open_orders():
    kraken.get_open_orders(True)
    return

def open_positions():
    kraken.get_open_positions()
    return kraken.get_open_positions()

# TODO uncomment buy/sells
