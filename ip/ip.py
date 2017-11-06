from errbot import BotPlugin, botcmd
import requests
import json

class ip(BotPlugin):

	@botcmd
	def ip(self, msg, args):
		r = requests.get('http://ip-api.com/json/'+ args)
		r.raise_for_status()

		json_result = json.loads(r.content.decode('utf-8'))

		#json_result = loc.json()
    
		if json_result['as'] != None:
			as_net = json_result['as']
		else:
			as_net = ""

		if json_result['query'] != None:
			ipaddr = json_result['query']
		else:
			ipaddr = ""

		if json_result['isp'] != None:
			isp = json_result['isp']
		else:
			isp = ""

		if json_result['country'] != None:
			country = json_result['country']
		else:
			country = ""

		if json_result['region'] != None:
			region = json_result['region']
		else:
			region = ""

		if json_result['city'] != None:
			city = json_result['city']
		else:
			city = ""

		if json_result['zip'] != None:
			postal = str(json_result['zip'])
		else:
			postal = ""

		if json_result['timezone'] != None:
			timezone = str(json_result['timezone'])
		else:
			timezone = ""

		if json_result['lat'] != None:
			latitude = str(json_result['lat'])
		else:
			latitude = ""

		if json_result['lon'] != None:
			longitude = str(json_result['lon'])
		else:
			longitude = ""

		value = "IP: " + ipaddr + "\n" + "AS: " + as_net + "\n" + "ISP: " +  isp + "\n" + "Country: " + country + "\n" + "Region: " + region + "\n" + "City: " + city + "\n" +  "Postal: " + postal + "\n" +  "Timezone: " + timezone + "\n" + "Latitude: " + latitude + "\n"  + "Longitude: " + longitude

		if msg.is_direct:
			self.send(msg.frm, value)
		else:
			self.send(msg.to, value)
