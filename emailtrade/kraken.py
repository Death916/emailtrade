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
API  = krakenex.api(API_KEY, PRIV_KEY)


kraken = KrakenAPI(API)
buyprice = ""
sellprice = ""


def marketcheck(TICKER):
    markets =  kraken.get_ohlc_data(TICKER)
    price = markets[0]['close'][0]
    print(TICKER, "price is ", price)
    return price


#done

def open_trade():

    buyprice = marketcheck(TICKER)
    balancedf = kraken.get_account_balance() 
    balance = balancedf.vol["ZUSD"]
    buy_amount = (balance / buyprice) - (balance / buyprice) * 0.0025
    kraken.add_standard_order(TICKER,)
    print("buying", buy_amount, "of", TICKER)
    hist.tradehist(
        "bought " + str(buy_amount) + " of " + TICKER+ " at " + str(buyprice)
    )
    return


def close_trade():

    sellprice = marketcheck(TICKER)

    sell_amount = trex.get_balance("ETH")["result"]["Available"]
    print(trex.sell_limit(TICKER, sell_amount, rate=sellprice))
    print("selling", sell_amount, "of", TICKER)
    hist.tradehist(
        "sold " + str(sell_amount) + " of " + TICKER+ " at " + str(sellprice)
    )
    hist.tradehist(
        "profit = "
        + "{:.25f}".format((sellprice * sell_amount) - (buyprice * sell_amount))
    )


def open_orders():
    kraken.get_open_orders(True)
    return
