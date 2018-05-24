#! python3

import imapclient
import pyzmail

imap = imapclient.IMAPClient('imap.gmail.com', ssl=True)
imap.login('email', 'pass')
imap.select_folder('CRYPTO/trade', readonly=True)


alert = imap.search(b'UNSEEN')

for num in range(0, 100000):
	if num in alert:
		uid = num


msg = imap.fetch([uid], [b'BODY[]', b'FLAGS'])


message = pyzmail.PyzMessage.factory(msg[uid][b'BODY[]'])

if 'strategy says sell now' in message.get_subject():
	print('sell signal found')
	print(message.get_subject())
elif 'strategy says buy now' in message.get_subject():
	print('buy signal found')
	print(message.get_subject())


else:

	print('failed')

class start_trade():

