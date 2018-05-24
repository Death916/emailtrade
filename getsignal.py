#! python3

import imapclient
import pyzmail
import glogin

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
	if trade == "buy":
		print('trade is a buy')

def start_sell():
	if trade == "sell":
		print('trade is a sell')



if 'strategy says sell now' in message.get_subject():
		print('sell signal found')
		print(message.get_subject())
		trade = "sell"

elif 'strategy says buy now' in message.get_subject():
	print('buy signal found')
	print(message.get_subject())
	trade = "buy"

else:

	print('failed')



#start_buy()
#start_sell()