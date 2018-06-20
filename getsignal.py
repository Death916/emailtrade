#! python3

import imapclient
import pyzmail
import glogin
import subprocess
import time
import psutil

#login to server

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


last_alert = 0


def kill(proc_pid):
	
	process = psutil.Process(proc_pid)
	for procs in process.children(recursive=True):
		procs.kill()
	process.kill()


def start_buy():
	
	print('trade is a buy')
	proc = subprocess.Popen(['taskmgr'], stdout=subprocess.PIPE, shell=True)
	global last_alert
	last_alert = "buy"
	time.sleep(5)
	kill(proc.pid)
	

def start_sell():

	print('trade is a sell')
	proc = subprocess.Popen(['taskmgr'], stdout=subprocess.PIPE, shell=True)
	global last_alert
	last_alert = "sell"
	time.sleep(5)
	kill(proc.pid)


def get_signal():
	try: 
		if 'strategy says sell now' in message.get_subject() or last_alert == 'buy':	
			print('sell signal found')
			print(message.get_subject())
			print('got sell signal')
			return "sell"

		elif 'strategy says buy now' in message.get_subject():
			print('buy signal found')
			print(message.get_subject())
			return "buy"
	except:
		print('failed')


last_uid = 0


while True:

	print('in loop')

	global uid
	gconnect()
	print(uid)
	signal = get_signal()

	try:

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
	
	time.sleep(500)

