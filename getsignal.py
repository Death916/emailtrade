#! python3

import imapclient
import pyzmail
import glogin
import subprocess
import time
import psutil
import trade

# login to server

def gconnect():
	imap = glogin.connect()
	imap.select_folder('CRYPTO/trade', readonly=True)
	alert = imap.search(b'UNSEEN')
	global uid
	# get all unseen uids
	for num in range(0, 100000):
		if num in alert:
			uid = num

	msg = imap.fetch([uid], [b'BODY[]', b'FLAGS'])
	global message
	message = pyzmail.PyzMessage.factory(msg[uid][b'BODY[]'])
	print('connected')

last_alert = 0


def kill(proc_pid):
	
	process = psutil.Process(proc_pid)
	for procs in process.children(recursive=True):
		procs.kill()
	process.kill()


def start_buy():
	
	print('trade is a buy')
	trade.open_trade(1)
	global last_alert
	last_alert = "buy"
	
	
def start_sell():

	print('trade is a sell')
	trade.close_trade(1)
	global last_alert
	last_alert = "sell"
	

def get_signal():
	try: 
		if 'strategy says sell now' in message.get_subject() or last_alert == 'buy':	
			print('sell signal found')
			coin = message.get_subject()
			print(coin)
			return "sell"

		elif last_alert == 'sell' or last_alert == 0:
			print('buy signal found')
			coin = message.get_subject()
			"""if 'ETHBTC' in coin:     # TODO check for current ticker to use
				print('true')
			else:
    				print('false') """
			print(coin)
			
			return "buy"
			
	except:
		print('failed')


last_uid = 0

def main():
	while True:

		global uid
		gconnect()
		print(uid)
		signal = get_signal()
		print(time.ctime())

		try:
			global last_uid
			if last_uid != uid:

				if signal == "buy" and last_alert != 'buy':
					start_buy()
					print(last_alert)
					last_uid = uid
				elif signal == "sell" and last_alert == "buy":
					start_sell()
					print(last_alert)
					last_uid = uid
			else:
				print('same uid')
		except:
			print(' fail')
		print(trade.open_orders())
		
		time.sleep(600)

if __name__ == '__main__':
    	main()
	

