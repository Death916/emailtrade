#! python3


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
	trade.open_trade(1)
	global last_alert
	last_alert = "buy"
	hist.tradehist('buy test')


def start_sell():
	print('trade is a sell')
	trade.close_trade(1)
	global last_alert
	last_alert = "sell"
	hist.tradehist('sell test')


def get_signal():
	# noinspection PyPep8
	try:
		global uid
		if last_alert == 'buy' and last_uid != uid:
			print('sell signal found')
			signal = 'sell'
			return signal

		elif last_alert == 'sell' or last_alert == 0:
			print('buy signal found')
			# coin = message.get_subject()
			signal = 'buy'
			return signal

	except:
		print('get_signal() failed')


last_uid = 0


def main():
	s = gconnect()

	s.idle()
	start_time = time.time()
	while True:

		responses = s.idle_check(30)
		print("Server sent:", responses if responses else "nothing")

		list_uid = ([i[0] for i in responses])
		global last_uid
		if list_uid:
			global uid
			print(list_uid[0])
			uid = list_uid[0]
			signal = get_signal()
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

		## for debugging only ## TODO: Remove when done

		elif last_uid == 0:
			uid = 0
			signal = get_signal()

			if signal == "buy" and last_alert != 'buy':
				start_buy()
				print('last alert was', last_alert)
				last_uid = uid
			elif signal == "sell" and last_alert == "buy":
				start_sell()
				print('last alert was ', last_alert)
				last_uid = uid
		##                  ##
		else:
			print('same uid')


		print(time.ctime())





		if trade.open_orders():
			print(trade.open_orders())

		if time.time() - start_time > 1740:
			s.idle_done()
			print('restarting connection')
			s.logout()
			s = gconnect()
			s.idle()
			start_time = time.time()


if __name__ == '__main__':
	main()
