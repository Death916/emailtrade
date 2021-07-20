
from ast import arg
from inspect import ArgSpec
from sqlite3 import Date
from symbol import arglist
import time
import csv
import pandas


TIME = "1200"
EXCHANGE = "kraken"
PRICE = "1800"
PROFIT = "30"
DATE = "10-10-14"
TYPE = "buy"
PAIR = "BTCUSD"


def tradehist(msg):
    log = open("tradehist.txt", 'a')
    log.write('\n' + time.ctime() + ' ' +  msg)
    log.close()


def tradecsv(DATE, *args):
    with open('/home/death/code/python/emailtrade/emailtrade/bottrades.csv','w', newline= '') as csvfile:
        
        args = {Date: DATE, 'Time': TIME, }
        tradewriter = csv.DictWriter(csvfile, fieldnames="Date, Time, Exchange, Price, Profit,Type, Pair")
        for i in args:
            tradewriter.writerow({i})
            tradewriter.writerows({'Date': DATE})
        csvfile.close

tradecsv([DATE],[TIME],[EXCHANGE],[PRICE],[PROFIT], [TYPE], [PAIR])
