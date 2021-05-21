import json
from bittrex import Bittrex
import history as hist
import os
import kraken

price = 0

with open(os.getcwd() + "/keys.json") as k:
    keys = json.load(k)


MARKET = input("Pease enter what market you want to use: Kraken or bittrex").lower()
# TODO add try/except for market to make sure its correct

class bittrex_trade():

    api_key = keys["api_key"]
    priv_key = keys["priv_key"]
    ticker = "BTC-ETH"
    trex = Bittrex(api_key, priv_key)


    def marketcheck(self, ticker):
        markets = trex.get_ticker(ticker)
        price = markets["result"]["Ask"]
        print(ticker, "price is ", price)
        return price


    buyprice = marketcheck(ticker)


    def open_trade(self):

        balance = trex.get_balance("BTC")["result"]["Available"]
        buy_amount = (balance / buyprice) - (balance / buyprice) * 0.0025
        print(trex.buy_limit(ticker, buy_amount, rate=buyprice))
        print("buying", buy_amount, "of", ticker)
        hist.tradehist(
            "bought " + str(buy_amount) + " of " + ticker + " at " + str(buyprice)
        )
        return


    def close_trade():

        sell_price = marketcheck(ticker)

        sell_amount = trex.get_balance("ETH")["result"]["Available"]
        print(trex.sell_limit(ticker, sell_amount, rate=sell_price))
        print("selling", sell_amount, "of", ticker)
        hist.tradehist(
            "sold " + str(sell_amount) + " of " + ticker + " at " + str(sell_price)
        )
        hist.tradehist(
            "profit = "
            + "{:.25f}".format((sell_price * sell_amount) - (buyprice * sell_amount))
        )


    def open_orders():
        trex.get_open_orders()
        return
