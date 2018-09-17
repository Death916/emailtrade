import imapclient
import json
with open('D:/code/emailtrade/keys.json') as k:
	keys = json.load(k)

def connect():
	email = keys['email']
	passw = keys['passw']

	server = imapclient.IMAPClient('imap.gmail.com', ssl=True)
	server.login(email, passw)
	print('login success')

	return server

