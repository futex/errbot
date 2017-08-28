import requests
import random
#from beautifulSoup import beautifulSoup
from errbot import BotPlugin, botcmd
from errcron.bot import CrontabMixin

class auto_beer(BotPlugin, CrontabMixin):

	CHANID="XXXXX"

	CRONTAB = [
		'00 18 * * 5 .auto_beer ' CHANID,
	]

	def get_configuration_template(self):
		""" configuration entries """
		config = {
			'api_key': '',
		}
		return config

	def _check_config(self, option):

		# if no config, return nothing
		if self.config is None:
			return None
		else:
	        # now, let's validate the key
			if option in self.config:
				return self.config[option]
			else:
				return None

	def _get_api_key(self):
		return self._check_config('api_key') or 'dc6zaTOxFJmzC'

	def activate(self):
		super(auto_beer, self).activate()
		self.activate_crontab()

	@botcmd
	def auto_beer(self, polled_time, identity):

		api_key = self._get_api_key()
		gif_size = 'original'
		max_image_size = 8000000

		params = {
			'q': 'beer',
			'limit': 20,
			'api_key': api_key,
		}

		r = requests.get('http://api.giphy.com/v1/gifs/search', params=params)
		self.log.debug('url sent: {}'.format(r.url))

		results = r.json()
		results_count = len(results['data'])
		self.log.debug('results found: {}'.format(results_count))

		if results_count != 0:
			response = None
			while response is None:
				image_number = random.randrange(0, results_count)
				image_size = int(results['data'][image_number]['images'][gif_size]['size'])
				# Restricting to max size limit
				if image_size < max_image_size:
					response = results['data'][image_number]['images'][gif_size]['url']
		else:
			response = 'No results found.'

		if "Telegram" in str(type(self._bot)) :
			self._bot.telegram.sendMessage(chat_id=CHANID, text="Week end!!!! Time to take a beer!")
			self._bot.telegram.sendMessage(chat_id=CHANID, text=response)
		
		#return response
