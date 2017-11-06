from errbot import BotPlugin, botcmd, arg_botcmd
import subprocess
import configparser
import ast
from googleapiclient.discovery import build
import ast

def google_search(search_term, api_key, cse_id, **kwargs):
	service = build("customsearch", "v1", developerKey=api_key)
	res = service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()
	if "items" in res:
		return res['items']
	else:
		return None

class urlquery(BotPlugin):


	@arg_botcmd('search', type=str)
	def urlquery(self, msg, search):
		"""
		Search on various Blog Website via CSE
		"""
		config = configparser.ConfigParser()
		config.read('config.conf')

		results = google_search("\""+search+"\"", ast.literal_eval(config['GSE']['APIKEY']), "013088570227507235128:pgp3a7q4h8e", num=10)
	   
		if results:
			for result in results:
				yield "urlquery -- " + result["displayLink"] + " -- " + result["link"]
		else:
				yield "urlquery -- No results in Google CSE"