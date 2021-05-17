import json

import history as hist
import os
import krakenex
from pykrakenapi import KrakenAPI


with open(os.getcwd() + "/keys.json") as k:
    keys = json.load(k)

API_KEY = keys["public"]
PRIV_KEY = keys["priv"]
TICKER = "ETHUSD"
API = krakenex.API(API_KEY, PRIV_KEY)
# BUY_COIN = input("what coin to buy")
# SELL_COIN = input("what to buy it with")
kraken = KrakenAPI(API)


def marketcheck():
    markets = kraken.get_ohlc_data(TICKER)
    price = markets[0]['close'][0]
    print(TICKER, "price is ", price)
    return price


# done
buyprice = marketcheck()


def open_trade():

    balancedf = kraken.get_account_balance() 
    balance = balancedf.vol["ZUSD"]
    buy_amount = (balance / buyprice) - (balance / buyprice) * 0.0025
    # kraken.add_standard_order(TICKER, "buy", "market", balance)
    print("buying", buy_amount, "of", TICKER, " for ", balance)
    hist.tradehist(
        "bought " + str(buy_amount) + " of " + TICKER + " at " + str(buyprice)
    )
    return buy_amount


def close_trade():

    sell_price = marketcheck()
    balancedf = kraken.get_account_balance()
    sell_amount = balancedf.vol['XETH']
    # print(kraken.add_standard_order(TICKER, "sell", "market", sell_amount))
    print("selling", sell_amount, "of", TICKER)
    hist.tradehist(
        "sold " + str(sell_amount) + " of " + TICKER + " at " + str(sell_price)
    )
    hist.tradehist(
        "profit = "
        + "{:.25f}".format((sell_price * sell_amount) - (buyprice * sell_amount))
    )


def open_orders():
    kraken.get_open_orders(True)
    return
