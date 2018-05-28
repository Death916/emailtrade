#! python3

import imapclient
import pyzmail
import glogin
import subprocess

#login to server
imap = glogin.connect()
imap.select_folder('CRYPTO/trade', readonly=True)
alert = imap.search(b'UNSEEN')

#get all unseen uids
for num in range(0, 100000):
	if num in alert:
		uid = num

msg = imap.fetch([uid], [b'BODY[]', b'FLAGS'])
message = pyzmail.PyzMessage.factory(msg[uid][b'BODY[]'])

trade = None

def start_buy():
	    print('trade is a buy')
	    subprocess.check_call(['/usr/local/bin/catalyst live -f buy_and_hodl.py -x poloniex -n test -c btc --capital-base 100'], shell = True)
    
    

def start_sell():
	if trade == "sell":
		print('trade is a sell')



def get_signal():
    try: 
        if 'strategy says sell now' in message.get_subject():	
            print('sell signal found')
            print(message.get_subject())
            return "sell"

        elif 'strategy says buy now' in message.get_subject():
            print('buy signal found')
            print(message.get_subject())
            return "buy"
    except:
        print('failed')



signal = get_signal()
if signal == "buy":
    start_buy()
if signal == "sell"
    start_sell()

