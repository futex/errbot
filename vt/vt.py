from errbot import BotPlugin, botcmd
import subprocess
import configparser
import ast

class vt(BotPlugin):

	@botcmd
	def vt(self, msg, args):

		Config = configparser.ConfigParser()
		Config.read("./config.conf")
		
		VTHASH_PATH=ast.literal_eval(Config.get("VT", "VTHASH_PATH"))
        
		output = subprocess.Popen([VTHASH_PATH, args], stdout=subprocess.PIPE).communicate()[0]

		if msg.is_direct:
			self.send(msg.frm, output.decode('unicode_escape'))
		else:
			self.send(msg.to, output.decode('unicode_escape'))
