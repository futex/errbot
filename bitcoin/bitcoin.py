from errbot import BotPlugin, botcmd
import requests
import json
import time
import cfscrape
from requests.packages.urllib3.exceptions import InsecureRequestWarning

class bitcoin(BotPlugin):

	headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:52.0) Gecko/20170101 Firefox/52.0'}

	@botcmd
	def bitcoin(self, msg, args):
			"""
			Check the Bitcoin value
			"""

			requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
			

			requests_flare = cfscrape.create_scraper()
			r = requests_flare.get("https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=BTC,USD,EUR", headers=self.headers)
			r.raise_for_status()

			data = json.loads(r.content.decode('utf-8'))
	    
			conversion_dollar = data['USD']
			conversion_euro = data['EUR']

			r = requests_flare.get("https://min-api.cryptocompare.com/data/histohour?fsym=BTC&tsym=USD&limit=1", headers=self.headers)

			dataset = json.loads(r.content.decode('utf-8'))

			oldValue = dataset['Data'][0]['high']
			currentValue = dataset['Data'][1]['high']

			diff =  currentValue - oldValue

			percent = round(diff / currentValue * 100, 2)

			if percent > 0:
				value = "1 bitcoin = %s EURO or %s USD. Average +%s%%" % (conversion_euro, conversion_dollar, percent)
			else:
				value = "1 bitcoin = %s EURO or %s USD. Average %s%%" % (conversion_euro, conversion_dollar, percent)

			return value

	@botcmd
	def ltc(self, msg, args):
			"""
			Check the Litecoin value
			"""

			requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
			requests_flare = cfscrape.create_scraper()
			r =requests_flare.get("https://min-api.cryptocompare.com/data/price?fsym=LTC&tsyms=BTC,USD,EUR", headers=self.headers)
			r.raise_for_status()

			data = json.loads(r.content.decode('utf-8'))
	    
			conversion_BTC = data['BTC']
			conversion_dollar = data['USD']
			conversion_euro = data['EUR']

			r = requests_flare.get("https://min-api.cryptocompare.com/data/histohour?fsym=LTC&tsym=USD&limit=1", headers=self.headers)

			dataset = json.loads(r.content.decode('utf-8'))

			oldValue = dataset['Data'][0]['high']
			currentValue = dataset['Data'][1]['high']

			diff =  currentValue - oldValue

			percent = round(diff / currentValue * 100, 2)

			if percent > 0:
				value = "1 Litecoin = %s EURO or %s USD or %s Bitcoin. Average +%s%%" % (conversion_euro, conversion_dollar, conversion_BTC, percent)	
			else:
				value = "1 Litecoin = %s EURO or %s USD or %s Bitcoin. Average %s%%" % (conversion_euro, conversion_dollar, conversion_BTC, percent)

			return value

	@botcmd
	def dsh(self, msg, args):
			"""
			Check the Dash value
			"""
			requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
			requests_flare = cfscrape.create_scraper()
			r =requests_flare.get("https://min-api.cryptocompare.com/data/price?fsym=DASH&tsyms=BTC,USD,EUR", headers=self.headers)
			r.raise_for_status()

			data = json.loads(r.content.decode('utf-8'))
	    
			conversion_BTC = data['BTC']
			conversion_dollar = data['USD']
			conversion_euro = data['EUR']

			r = requests_flare.get("https://min-api.cryptocompare.com/data/histohour?fsym=DASH&tsym=USD&limit=1", headers=self.headers)

			dataset = json.loads(r.content.decode('utf-8'))

			oldValue = dataset['Data'][0]['high']
			currentValue = dataset['Data'][1]['high']

			diff =  currentValue - oldValue

			percent = round(diff / currentValue * 100, 2)

			if percent > 0:
				value = "1 Dash = %s EURO or %s USD or %s Bitcoin. Average +%s%%" % (conversion_euro, conversion_dollar, conversion_BTC, percent)	
			else:
				value = "1 Dash = %s EURO or %s USD or %s Bitcoin. Average %s%%" % (conversion_euro, conversion_dollar, conversion_BTC, percent)

			return value

	@botcmd
	def xrp(self, msg, args):
			"""
			Check the Ripple value
			"""
			requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
			requests_flare = cfscrape.create_scraper()
			r =requests_flare.get("https://min-api.cryptocompare.com/data/price?fsym=XRP&tsyms=BTC,USD,EUR", headers=self.headers)
			r.raise_for_status()

			data = json.loads(r.content.decode('utf-8'))
	    
			conversion_BTC = data['BTC']
			conversion_dollar = data['USD']
			conversion_euro = data['EUR']

			r = requests_flare.get("https://min-api.cryptocompare.com/data/histohour?fsym=XRP&tsym=USD&limit=1", headers=self.headers)

			dataset = json.loads(r.content.decode('utf-8'))

			oldValue = dataset['Data'][0]['high']
			currentValue = dataset['Data'][1]['high']

			diff =  currentValue - oldValue

			percent = round(diff / currentValue * 100, 2)

			if percent > 0:
				value = "1 Ripple = %s EURO or %s USD or %s Bitcoin. Average +%s%%" % (conversion_euro, conversion_dollar, conversion_BTC, percent)	
			else:
				value = "1 Ripple = %s EURO or %s USD or %s Bitcoin. Average %s%%" % (conversion_euro, conversion_dollar, conversion_BTC, percent)

			return value

	@botcmd
	def xmr(self, msg, args):
			"""
			Check the Monero value
			"""
			requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
			requests_flare = cfscrape.create_scraper()
			r =requests_flare.get("https://min-api.cryptocompare.com/data/price?fsym=XMR&tsyms=BTC,USD,EUR", headers=self.headers)
			r.raise_for_status()

			data = json.loads(r.content.decode('utf-8'))
	    
			conversion_BTC = data['BTC']
			conversion_dollar = data['USD']
			conversion_euro = data['EUR']

			r = requests_flare.get("https://min-api.cryptocompare.com/data/histohour?fsym=XMR&tsym=USD&limit=1", headers=self.headers)

			dataset = json.loads(r.content.decode('utf-8'))

			oldValue = dataset['Data'][0]['high']
			currentValue = dataset['Data'][1]['high']

			diff =  currentValue - oldValue

			percent = round(diff / currentValue * 100, 2)

			if percent > 0:
				value = "1 Monero = %s EURO or %s USD or %s Bitcoin. Average +%s%%" % (conversion_euro, conversion_dollar, conversion_BTC, percent)	
			else:
				value = "1 Monero = %s EURO or %s USD or %s Bitcoin. Average %s%%" % (conversion_euro, conversion_dollar, conversion_BTC, percent)

			return value


	@botcmd
	def doge(self, msg, args):
			"""
			Check the Dogecoin value
			"""
			requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
			requests_flare = cfscrape.create_scraper()
			r =requests_flare.get("https://min-api.cryptocompare.com/data/price?fsym=DOGE&tsyms=BTC,USD,EUR", headers=self.headers)
			r.raise_for_status()

			data = json.loads(r.content.decode('utf-8'))
	    
			conversion_BTC = data['BTC']
			conversion_dollar = data['USD']
			conversion_euro = data['EUR']

			r = requests_flare.get("https://min-api.cryptocompare.com/data/histohour?fsym=DOGE&tsym=USD&limit=1", headers=self.headers)

			dataset = json.loads(r.content.decode('utf-8'))

			oldValue = dataset['Data'][0]['high']
			currentValue = dataset['Data'][1]['high']

			diff =  currentValue - oldValue

			percent = round(diff / currentValue * 100, 2)

			if percent > 0:
				value = "1 Dogecoin = %s EURO or %s USD or %s Bitcoin. Average +%s%%" % (conversion_euro, conversion_dollar, conversion_BTC, percent)	
			else:
				value = "1 Dogecoin = %s EURO or %s USD or %s Bitcoin. Average %s%%" % (conversion_euro, conversion_dollar, conversion_BTC, percent)


			return value


	@botcmd
	def eth(self, msg, args):
			"""
			Check the Ethereum value
			"""

			#last hour https://min-api.cryptocompare.com/data/histohour?fsym=ETH&tsym=USD&limit=1
			requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
			requests_flare = cfscrape.create_scraper()
			r =requests_flare.get("https://min-api.cryptocompare.com/data/price?fsym=ETH&tsyms=BTC,USD,EUR", headers=self.headers)
			r.raise_for_status()

			data = json.loads(r.content.decode('utf-8'))
	    
			conversion_BTC = data['BTC']
			conversion_dollar = data['USD']
			conversion_euro = data['EUR']

			r = requests_flare.get("https://min-api.cryptocompare.com/data/histohour?fsym=ETH&tsym=USD&limit=1", headers=self.headers)

			dataset = json.loads(r.content.decode('utf-8'))

			oldValue = dataset['Data'][0]['high']
			currentValue = dataset['Data'][1]['high']

			diff =  currentValue - oldValue

			percent = round(diff / currentValue * 100, 2)

			if percent > 0:
				value = "1 Ethereum = %s EURO or %s USD or %s Bitcoin. Average +%s%%" % (conversion_euro, conversion_dollar, conversion_BTC, percent)	
			else:
				value = "1 Ethereum = %s EURO or %s USD or %s Bitcoin. Average %s%%" % (conversion_euro, conversion_dollar, conversion_BTC, percent)

			return value

	@botcmd
	def zec(self, msg, args):
			"""
			Check the Zcash value
			"""
			requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
			requests_flare = cfscrape.create_scraper()
			r =requests_flare.get("https://min-api.cryptocompare.com/data/price?fsym=ZEC&tsyms=BTC,USD,EUR", headers=self.headers)
			r.raise_for_status()

			data = json.loads(r.content.decode('utf-8'))
	    
			conversion_BTC = data['BTC']
			conversion_dollar = data['USD']
			conversion_euro = data['EUR']

			r = requests_flare.get("https://min-api.cryptocompare.com/data/histohour?fsym=ZEC&tsym=USD&limit=1", headers=self.headers)

			dataset = json.loads(r.content.decode('utf-8'))

			oldValue = dataset['Data'][0]['high']
			currentValue = dataset['Data'][1]['high']

			diff =  currentValue - oldValue

			percent = round(diff / currentValue * 100, 2)

			if percent > 0:
				value = "1 zcash = %s EURO or %s USD or %s Bitcoin. Average +%s%%" % (conversion_euro, conversion_dollar, conversion_BTC, percent)
			else:	
				value = "1 zcash = %s EURO or %s USD or %s Bitcoin. Average %s%%" % (conversion_euro, conversion_dollar, conversion_BTC, percent)

			return value

	@botcmd
	def bch(self, msg, args):
			"""
			Check the bitcoin cash value
			"""
			requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
			requests_flare = cfscrape.create_scraper()
			r =requests_flare.get("https://min-api.cryptocompare.com/data/price?fsym=BCH&tsyms=BTC,USD,EUR", headers=self.headers)
			r.raise_for_status()

			data = json.loads(r.content.decode('utf-8'))
	    
			conversion_BTC = data['BTC']
			conversion_dollar = data['USD']
			conversion_euro = data['EUR']

			r = requests_flare.get("https://min-api.cryptocompare.com/data/histohour?fsym=BCH&tsym=USD&limit=1", headers=self.headers)

			dataset = json.loads(r.content.decode('utf-8'))

			oldValue = dataset['Data'][0]['high']
			currentValue = dataset['Data'][1]['high']

			diff =  currentValue - oldValue

			percent = round(diff / currentValue * 100, 2)

			if percent > 0:
				value = "1 Bitcoin cash = %s EURO or %s USD or %s Bitcoin. Average +%s%%" % (conversion_euro, conversion_dollar, conversion_BTC, percent)
			else:	
				value = "1 Bitcoin cash = %s EURO or %s USD or %s Bitcoin. Average %s%%" % (conversion_euro, conversion_dollar, conversion_BTC, percent)

			return value

	@botcmd
	def neo(self, msg, args):
			"""
			Check the neo value
			"""
			requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
			requests_flare = cfscrape.create_scraper()
			r =requests_flare.get("https://min-api.cryptocompare.com/data/price?fsym=NEO&tsyms=BTC,USD,EUR", headers=self.headers)
			r.raise_for_status()

			data = json.loads(r.content.decode('utf-8'))
	    
			conversion_BTC = data['BTC']
			conversion_dollar = data['USD']
			conversion_euro = data['EUR']

			r = requests_flare.get("https://min-api.cryptocompare.com/data/histohour?fsym=NEO&tsym=USD&limit=1", headers=self.headers)

			dataset = json.loads(r.content.decode('utf-8'))

			oldValue = dataset['Data'][0]['high']
			currentValue = dataset['Data'][1]['high']

			diff =  currentValue - oldValue

			percent = round(diff / currentValue * 100, 2)

			if percent > 0:
				value = "1 Neo = %s EURO or %s USD or %s Bitcoin. Average +%s%%" % (conversion_euro, conversion_dollar, conversion_BTC, percent)
			else:	
				value = "1 Neo = %s EURO or %s USD or %s Bitcoin. Average %s%%" % (conversion_euro, conversion_dollar, conversion_BTC, percent)

			return value

	@botcmd
	def xlm(self, msg, args):
			"""
			Check the Lumen value
			"""
			requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
			requests_flare = cfscrape.create_scraper()
			r =requests_flare.get("https://min-api.cryptocompare.com/data/price?fsym=XLM&tsyms=BTC,USD,EUR", headers=self.headers)
			r.raise_for_status()

			data = json.loads(r.content.decode('utf-8'))
	    
			conversion_BTC = data['BTC']
			conversion_dollar = data['USD']
			conversion_euro = data['EUR']

			r = requests_flare.get("https://min-api.cryptocompare.com/data/histohour?fsym=XLM&tsym=USD&limit=1", headers=self.headers)

			dataset = json.loads(r.content.decode('utf-8'))

			oldValue = dataset['Data'][0]['high']
			currentValue = dataset['Data'][1]['high']

			diff =  currentValue - oldValue

			percent = round(diff / currentValue * 100, 2)

			if percent > 0:
				value = "1 Stellar = %s EURO or %s USD or %s Bitcoin. Average +%s%%" % (conversion_euro, conversion_dollar, conversion_BTC, percent)
			else:	
				value = "1 Stellar = %s EURO or %s USD or %s Bitcoin. Average %s%%" % (conversion_euro, conversion_dollar, conversion_BTC, percent)

			return value

	@botcmd
	def omg(self, msg, args):
			"""
			Check the omisego value
			"""
			requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
			requests_flare = cfscrape.create_scraper()
			r =requests_flare.get("https://min-api.cryptocompare.com/data/price?fsym=OMG&tsyms=BTC,USD,EUR", headers=self.headers)
			r.raise_for_status()

			data = json.loads(r.content.decode('utf-8'))
	    
			conversion_BTC = data['BTC']
			conversion_dollar = data['USD']
			conversion_euro = data['EUR']

			r = requests_flare.get("https://min-api.cryptocompare.com/data/histohour?fsym=OMG&tsym=USD&limit=1", headers=self.headers)

			dataset = json.loads(r.content.decode('utf-8'))

			oldValue = dataset['Data'][0]['high']
			currentValue = dataset['Data'][1]['high']

			diff =  currentValue - oldValue

			percent = round(diff / currentValue * 100, 2)

			if percent > 0:
				value = "1 OmiseGO = %s EURO or %s USD or %s Bitcoin. Average +%s%%" % (conversion_euro, conversion_dollar, conversion_BTC, percent)
			else:	
				value = "1 OmiseGO = %s EURO or %s USD or %s Bitcoin. Average %s%%" % (conversion_euro, conversion_dollar, conversion_BTC, percent)

			return value

	@botcmd
	def iot(self, msg, args):
			"""
			Check the omisego value
			"""
			requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
			requests_flare = cfscrape.create_scraper()
			r =requests_flare.get("https://min-api.cryptocompare.com/data/price?fsym=IOT&tsyms=BTC,USD,EUR", headers=self.headers)
			r.raise_for_status()

			data = json.loads(r.content.decode('utf-8'))
	    
			conversion_BTC = data['BTC']
			conversion_dollar = data['USD']
			conversion_euro = data['EUR']

			r = requests_flare.get("https://min-api.cryptocompare.com/data/histohour?fsym=IOT&tsym=USD&limit=1", headers=self.headers)

			dataset = json.loads(r.content.decode('utf-8'))

			oldValue = dataset['Data'][0]['high']
			currentValue = dataset['Data'][1]['high']

			diff =  currentValue - oldValue

			percent = round(diff / currentValue * 100, 2)

			if percent > 0:
				value = "1 Iota = %s EURO or %s USD or %s Bitcoin. Average +%s%%" % (conversion_euro, conversion_dollar, conversion_BTC, percent)
			else:	
				value = "1 Iota = %s EURO or %s USD or %s Bitcoin. Average %s%%" % (conversion_euro, conversion_dollar, conversion_BTC, percent)

			return value

	@botcmd
	def rdd(self, msg, args):
			"""
			Check the omisego value
			"""
			requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
			requests_flare = cfscrape.create_scraper()
			r =requests_flare.get("https://min-api.cryptocompare.com/data/price?fsym=RDD&tsyms=BTC,USD,EUR", headers=self.headers)
			r.raise_for_status()

			data = json.loads(r.content.decode('utf-8'))
	    
			conversion_BTC = data['BTC']
			conversion_dollar = data['USD']
			conversion_euro = data['EUR']

			r = requests_flare.get("https://min-api.cryptocompare.com/data/histohour?fsym=RDD&tsym=USD&limit=1", headers=self.headers)

			dataset = json.loads(r.content.decode('utf-8'))

			oldValue = dataset['Data'][0]['high']
			currentValue = dataset['Data'][1]['high']

			diff =  currentValue - oldValue

			percent = round(diff / currentValue * 100, 2)

			if percent > 0:
				value = "1 Reddcoin = %s EURO or %s USD or %s Bitcoin. Average +%s%%" % (conversion_euro, conversion_dollar, conversion_BTC, percent)
			else:	
				value = "1 Reddcoin = %s EURO or %s USD or %s Bitcoin. Average %s%%" % (conversion_euro, conversion_dollar, conversion_BTC, percent)

			return value

	@botcmd
	def etc(self, msg, args):
			"""
			Check the omisego value
			"""
			requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
			requests_flare = cfscrape.create_scraper()
			r =requests_flare.get("https://min-api.cryptocompare.com/data/price?fsym=ETC&tsyms=BTC,USD,EUR", headers=self.headers)
			r.raise_for_status()

			data = json.loads(r.content.decode('utf-8'))
	    
			conversion_BTC = data['BTC']
			conversion_dollar = data['USD']
			conversion_euro = data['EUR']

			r = requests_flare.get("https://min-api.cryptocompare.com/data/histohour?fsym=ETC&tsym=USD&limit=1", headers=self.headers)

			dataset = json.loads(r.content.decode('utf-8'))

			oldValue = dataset['Data'][0]['high']
			currentValue = dataset['Data'][1]['high']

			diff =  currentValue - oldValue

			percent = round(diff / currentValue * 100, 2)

			if percent > 0:
				value = "1 Ethereum Classic = %s EURO or %s USD or %s Bitcoin. Average +%s%%" % (conversion_euro, conversion_dollar, conversion_BTC, percent)
			else:	
				value = "1 Ethereum Classic = %s EURO or %s USD or %s Bitcoin. Average %s%%" % (conversion_euro, conversion_dollar, conversion_BTC, percent)

			return value

	@botcmd
	def xvg(self, msg, args):
			"""
			Check the omisego value
			"""
			requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
			requests_flare = cfscrape.create_scraper()
			r =requests_flare.get("https://min-api.cryptocompare.com/data/price?fsym=XVG&tsyms=BTC,USD,EUR", headers=self.headers)
			r.raise_for_status()

			data = json.loads(r.content.decode('utf-8'))
	    
			conversion_BTC = data['BTC']
			conversion_dollar = data['USD']
			conversion_euro = data['EUR']

			r = requests_flare.get("https://min-api.cryptocompare.com/data/histohour?fsym=XVG&tsym=USD&limit=1", headers=self.headers)

			dataset = json.loads(r.content.decode('utf-8'))

			oldValue = dataset['Data'][0]['high']
			currentValue = dataset['Data'][1]['high']

			diff =  currentValue - oldValue

			percent = round(diff / currentValue * 100, 2)

			if percent > 0:
				value = "1 Verge = %s EURO or %s USD or %s Bitcoin. Average +%s%%" % (conversion_euro, conversion_dollar, conversion_BTC, percent)
			else:	
				value = "1 Verge = %s EURO or %s USD or %s Bitcoin. Average %s%%" % (conversion_euro, conversion_dollar, conversion_BTC, percent)

			return value

	@botcmd
	def lepen(self, msg, args):
			"""
			Check the omisego value
			"""
			requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
			requests_flare = cfscrape.create_scraper()
			r =requests_flare.get("https://min-api.cryptocompare.com/data/price?fsym=LEPEN&tsyms=BTC,USD,EUR", headers=self.headers)
			r.raise_for_status()

			data = json.loads(r.content.decode('utf-8'))
	    
			conversion_BTC = data['BTC']
			conversion_dollar = data['USD']
			conversion_euro = data['EUR']

			r = requests_flare.get("https://min-api.cryptocompare.com/data/histohour?fsym=LEPEN&tsym=USD&limit=1", headers=self.headers)

			dataset = json.loads(r.content.decode('utf-8'))

			oldValue = dataset['Data'][0]['high']
			currentValue = dataset['Data'][1]['high']

			diff =  currentValue - oldValue

			percent = round(diff / currentValue * 100, 2)

			if percent > 0:
				value = "1 Lepen Coin = %s EURO or %s USD or %s Bitcoin. Average +%s%%" % (conversion_euro, conversion_dollar, conversion_BTC, percent)
			else:	
				value = "1 Lepen Coin = %s EURO or %s USD or %s Bitcoin. Average %s%%" % (conversion_euro, conversion_dollar, conversion_BTC, percent)

			return value
	@botcmd
	def macron(self, msg, args):
			"""
			Check the omisego value
			"""
			requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
			requests_flare = cfscrape.create_scraper()
			r =requests_flare.get("https://min-api.cryptocompare.com/data/price?fsym=MCRN&tsyms=BTC,USD,EUR", headers=self.headers)
			r.raise_for_status()

			data = json.loads(r.content.decode('utf-8'))
	    
			conversion_BTC = data['BTC']
			conversion_dollar = data['USD']
			conversion_euro = data['EUR']

			r = requests_flare.get("https://min-api.cryptocompare.com/data/histohour?fsym=MCRN&tsym=USD&limit=1", headers=self.headers)

			dataset = json.loads(r.content.decode('utf-8'))

			oldValue = dataset['Data'][0]['high']
			currentValue = dataset['Data'][1]['high']

			diff =  currentValue - oldValue

			percent = round(diff / currentValue * 100, 2)

			if percent > 0:
				value = "1 Macron Coin = %s EURO or %s USD or %s Bitcoin. Average +%s%%" % (conversion_euro, conversion_dollar, conversion_BTC, percent)
			else:	
				value = "1 Macron Coin = %s EURO or %s USD or %s Bitcoin. Average %s%%" % (conversion_euro, conversion_dollar, conversion_BTC, percent)

			return value


	@botcmd
	def coincoin(self, msg, args):
		rtn = self.bitcoin(msg, args)
		rtn += "\n" + self.bch(msg, args)
		rtn += "\n" + self.ltc(msg, args)	
		rtn += "\n" + self.eth(msg, args)
		rtn += "\n" + self.zec(msg, args)
		rtn += "\n" + self.dsh(msg, args)
		rtn += "\n" + self.xmr(msg, args)
		rtn += "\n" + self.xrp(msg, args)
		rtn += "\n" + self.doge(msg, args)
		rtn += "\n" + self.neo(msg, args)
		rtn += "\n" + self.xlm(msg, args)
		rtn += "\n" + self.omg(msg, args)
		rtn += "\n" + self.iot(msg, args)
		rtn += "\n" + self.rdd(msg, args)
		rtn += "\n" + self.etc(msg, args)
		rtn += "\n" + self.xvg(msg, args)
		rtn += "\n" + self.lepen(msg, args)
		rtn += "\n" + self.macron(msg, args)

		return rtn

	#https://min-api.cryptocompare.com/data/price?fsym=ETH&tsyms=BTC,USD,EUR