import feedparser
import requests
import re
from bs4 import BeautifulSoup as bs
from errbot import BotPlugin, botcmd
from errcron.bot import CrontabMixin

class auto_bonjour(BotPlugin, CrontabMixin):

	CHANID="XXXXXX"

	CRONTAB = [
		'00 12 * * 1-5 .bonjourmadame ' CHANID,
		'00 12 * * 0,6 .bonjourmabelle ' CHANID,
	]

	def activate(self):
		super(auto_bonjour, self).activate()
		self.activate_crontab()

	def cleanhtml(self, raw_html):
		cleanr = re.compile('<.*?>')
		cleantext = re.sub(cleanr, '', raw_html)
		return cleantext

	@botcmd
	def bonjourmadame(self, polled_time, identity):
		"""
		Bonjour Madame
		"""

		bjr_path = "/tmp/bonjour.jpg"
		madames = feedparser.parse("http://feeds2.feedburner.com/BonjourMadame")
		#bm_text = madames['entries'][0]['summary_detail']['value'].split('<p>')[1].replace('</p>','')
		#bm_text = madames['entries'][0]['title']
		#bm_text = beautifulSoup(madames['entries'][0]['title']).text
		bm_text = self.cleanhtml(madames['entries'][0]['title'])
		madame_du_jour = madames['entries'][0]['summary_detail']['value'].split('"')[1]

		r = requests.get(madame_du_jour, stream=True)

		if r.status_code == 200:
			with open(bjr_path, 'wb') as f:
				f.write(r.content)

		if "Telegram" in str(type(self._bot)) :
			self._bot.telegram.sendMessage(chat_id=CHANID, text=bm_text)
			self._bot.telegram.sendPhoto(chat_id=CHANID, photo=open(bjr_path,"rb"))
		else:
			return madame_du_jour

	@botcmd
	def bonjourmabelle(self, polled_time, identity):
		"""
		Bonjour ma belle
		"""

		URL="http://bonjourmabelle.fr/"
		bjr_path = "/tmp/bonjour.jpg"

		r = requests.get(URL, stream=True)

		if r.status_code == 200:

			soup = bs(r.content, "lxml")
			parsed = list(r.content)

			for image in soup.findAll("img"):
			
				filename = "%(src)s" % image
						
				if "media.tumblr.com" in filename:
					
					r = requests.get(filename, stream=True)

					if r.status_code == 200:
						with open(bjr_path, 'wb') as f:
							f.write(r.content)

						if "Telegram" in str(type(self._bot)) :
							self._bot.telegram.sendMessage(chat_id=CHANID,text="bonjour Ma Belle")
							self._bot.telegram.sendPhoto(chat_id=CHANID, photo=open(bjr_path,"rb"))
						else:
							return filename

						break

	@botcmd
	def auto_bonjour(self, polled_time, identity):
		self.bonjourMadame()
		self.bonjourMaBelle()


