from errbot import BotPlugin, botcmd
import requests
import json

class bitcoin(BotPlugin):

	@botcmd
	def bitcoin(self, msg, args):
			"""
			Check the Bitcoin value
			"""
			r =requests.get("https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=BTC,USD,EUR", stream=True)
			r.raise_for_status()

			data = json.loads(r.content.decode('utf-8'))
	    
			conversion_dollar = data['USD']
			conversion_euro = data['EUR']

			r = requests.get("https://min-api.cryptocompare.com/data/histohour?fsym=BTC&tsym=USD&limit=1", stream=True)

			dataset = json.loads(r.content.decode('utf-8'))

			oldValue = dataset['Data'][0]['high']
			currentValue = dataset['Data'][1]['high']

			diff =  currentValue - oldValue

			percent = round(diff / currentValue * 100, 2)

			if percent > 0:
				value = "1 bitcoin = %s EURO or %s USD. Average +%s%%" % (conversion_euro, conversion_dollar, percent)
			else:
				value = "1 bitcoin = %s EURO or %s USD. Average %s%%" % (conversion_euro, conversion_dollar, percent)

			if msg.is_direct:
				self.send(msg.frm, value)
			else:
				self.send(msg.to, value)

	@botcmd
	def ltc(self, msg, args):
			"""
			Check the Litecoin value
			"""
			r =requests.get("https://min-api.cryptocompare.com/data/price?fsym=LTC&tsyms=BTC,USD,EUR", stream=True)
			r.raise_for_status()

			data = json.loads(r.content.decode('utf-8'))
	    
			conversion_BTC = data['BTC']
			conversion_dollar = data['USD']
			conversion_euro = data['EUR']

			r = requests.get("https://min-api.cryptocompare.com/data/histohour?fsym=LTC&tsym=USD&limit=1", stream=True)

			dataset = json.loads(r.content.decode('utf-8'))

			oldValue = dataset['Data'][0]['high']
			currentValue = dataset['Data'][1]['high']

			diff =  currentValue - oldValue

			percent = round(diff / currentValue * 100, 2)

			if percent > 0:
				value = "1 Litecoin = %s EURO or %s USD or %s Bitcoin. Average +%s%%" % (conversion_euro, conversion_dollar, conversion_BTC, percent)	
			else:
				value = "1 Litecoin = %s EURO or %s USD or %s Bitcoin. Average %s%%" % (conversion_euro, conversion_dollar, conversion_BTC, percent)

			if msg.is_direct:
				self.send(msg.frm, value)
			else:
				self.send(msg.to, value)

	@botcmd
	def eth(self, msg, args):
			"""
			Check the Ethereum value
			"""

			#last hour https://min-api.cryptocompare.com/data/histohour?fsym=ETH&tsym=USD&limit=1
			r =requests.get("https://min-api.cryptocompare.com/data/price?fsym=ETH&tsyms=BTC,USD,EUR", stream=True)
			r.raise_for_status()

			data = json.loads(r.content.decode('utf-8'))
	    
			conversion_BTC = data['BTC']
			conversion_dollar = data['USD']
			conversion_euro = data['EUR']

			r = requests.get("https://min-api.cryptocompare.com/data/histohour?fsym=ETH&tsym=USD&limit=1", stream=True)

			dataset = json.loads(r.content.decode('utf-8'))

			oldValue = dataset['Data'][0]['high']
			currentValue = dataset['Data'][1]['high']

			diff =  currentValue - oldValue

			percent = round(diff / currentValue * 100, 2)

			if percent > 0:
				value = "1 Ethereum = %s EURO or %s USD or %s Bitcoin. Average +%s%%" % (conversion_euro, conversion_dollar, conversion_BTC, percent)	
			else:
				value = "1 Ethereum = %s EURO or %s USD or %s Bitcoin. Average %s%%" % (conversion_euro, conversion_dollar, conversion_BTC, percent)

			if msg.is_direct:
				self.send(msg.frm, value)
			else:
				self.send(msg.to, value)

	@botcmd
	def zec(self, msg, args):
			"""
			Check the Zcash value
			"""

			r =requests.get("https://min-api.cryptocompare.com/data/price?fsym=ZEC&tsyms=BTC,USD,EUR", stream=True)
			r.raise_for_status()

			data = json.loads(r.content.decode('utf-8'))
	    
			conversion_BTC = data['BTC']
			conversion_dollar = data['USD']
			conversion_euro = data['EUR']

			r = requests.get("https://min-api.cryptocompare.com/data/histohour?fsym=ZEC&tsym=USD&limit=1", stream=True)

			dataset = json.loads(r.content.decode('utf-8'))

			oldValue = dataset['Data'][0]['high']
			currentValue = dataset['Data'][1]['high']

			diff =  currentValue - oldValue

			percent = round(diff / currentValue * 100, 2)

			if percent > 0:
				value = "1 zcash = %s EURO or %s USD or %s Bitcoin. Average +%s%%" % (conversion_euro, conversion_dollar, conversion_BTC, percent)
			else:	
				value = "1 zcash = %s EURO or %s USD or %s Bitcoin. Average %s%%" % (conversion_euro, conversion_dollar, conversion_BTC, percent)

			if msg.is_direct:
				self.send(msg.frm, value)
			else:
				self.send(msg.to, value)

	@botcmd
	def bch(self, msg, args):
			"""
			Check the Zcash value
			"""

			r =requests.get("https://min-api.cryptocompare.com/data/price?fsym=BCH&tsyms=BTC,USD,EUR", stream=True)
			r.raise_for_status()

			data = json.loads(r.content.decode('utf-8'))
	    
			conversion_BTC = data['BTC']
			conversion_dollar = data['USD']
			conversion_euro = data['EUR']

			r = requests.get("https://min-api.cryptocompare.com/data/histohour?fsym=BCH&tsym=USD&limit=1", stream=True)

			dataset = json.loads(r.content.decode('utf-8'))

			oldValue = dataset['Data'][0]['high']
			currentValue = dataset['Data'][1]['high']

			diff =  currentValue - oldValue

			percent = round(diff / currentValue * 100, 2)

			if percent > 0:
				value = "1 Bitcoin cash = %s EURO or %s USD or %s Bitcoin. Average +%s%%" % (conversion_euro, conversion_dollar, conversion_BTC, percent)
			else:	
				value = "1 Bitcoin cash = %s EURO or %s USD or %s Bitcoin. Average %s%%" % (conversion_euro, conversion_dollar, conversion_BTC, percent)

			if msg.is_direct:
				self.send(msg.frm, value)
			else:
				self.send(msg.to, value)

	@botcmd
	def coincoin(self, msg, args):
		self.bitcoin(msg, args)
		self.bch(msg, args)
		self.ltc(msg, args)
		self.eth(msg, args)
		self.zec(msg, args)

	#https://min-api.cryptocompare.com/data/price?fsym=ETH&tsyms=BTC,USD,EUR