#! python3

import imapclient
import pyzmail
import glogin
import subprocess
import os
import signal
import time
import psutil

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

def kill(proc_pid):
    process = psutil.Process(proc_pid)
    for procs in process.children(recursive=True):
        procs.kill()
    process.kill()

def start_buy():
	if trade == "buy":
		print('trade is a buy')
		proc = subprocess.Popen(['taskmgr'], stdout=subprocess.PIPE, shell=True)
		time.sleep(5)
		kill(proc.pid)
		

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



start_buy()
#start_sell() 