import imapclient
import json
import os

with open(os.getcwd() + 'keys.json') as k:
	keys = json.load(k)

def connect():
	email = keys['email']
	passw = keys['passw']

	server = imapclient.IMAPClient('imap.gmail.com', ssl=True)
	server.login(email, passw)
	print('login success')

	return server

