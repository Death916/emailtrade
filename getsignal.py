#! python3

import imapclient
import pyzmail

imap = imapclient.IMAPClient('imap.gmail.com', ssl=True)
imap.login('tavn1992@gmail.com', 'tzzjgbzdtadlflls')
imap.select_folder('CRYPTO/trade', readonly=True)
msg = imap.fetch([3], [b'BODY[]', b'FLAGS'])

message = pyzmail.PyzMessage.factory(msg[3][b'BODY[]'])

print(message.get_subject())