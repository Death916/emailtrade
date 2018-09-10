import glogin
import trade
import history as hist

import time


# login to server

def gconnect():
    imap = glogin.connect()
    imap.select_folder('CRYPTO/trade', readonly=True)
    return imap

last_alert = 0

def start_buy():
    print('trade is a buy')
    trade.open_trade()
    global last_alert
    last_alert = "buy"
    hist.tradehist('buy test')


def start_sell():
    
    print('trade is a sell')
    trade.close_trade()
    global last_alert
    last_alert = "sell"
    hist.tradehist('sell test')


def getsignal():
    try:
        global uid
        if last_alert == 'buy' and last_uid != uid:
            print('sell signal found')
            return "sell"

        elif last_alert == 'sell' or last_alert == 0:
            print('buy signal found')
            return"buy"

    except:
        print('failed')


last_uid = 0


def main():
    s = gconnect()
    s.idle()
    start_time = time.time()
    while True:

        responses = s.idle_check(30)
        print("Server sent:", responses if responses else "nothing")


        list_uid = ([i[0] for i in responses])
        if list_uid != []:
            global uid
            print(list_uid[0])
            uid = list_uid[0]
            signal = getsignal()
        else:
            uid = 0

        print(time.ctime())
        global last_alert
        print('last alert was ', last_alert)


        global last_uid

        if last_uid != uid:

            if signal == "buy" and last_alert != 'buy':
                start_buy()
                print('last alert was', last_alert)
                last_uid = uid
            elif signal == "sell" and last_alert == "buy":
                start_sell()
                print('last alert was ', last_alert)
                last_uid = uid
        else:
            print('same uid')

        if trade.open_orders() != None:
            print(trade.open_orders())
        if time.time() - start_time > 1740:
            try:
                s.idle_done()
                print('restarting connection')
                s = gconnect()
                s.idle()
                start_time = time.time()
            except:
                print('restart failed trying again')
                s = gconnect()
                s.idle()
                start_time = time.time()




if __name__ == '__main__':
    main()
