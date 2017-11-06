from errbot import BotPlugin, botcmd
import subprocess

class shodan(BotPlugin):

	@botcmd(split_args_with=None)
	def shodan(self, msg, args):
		try:
       
			output = subprocess.Popen(["shodan"] + args, stdout=subprocess.PIPE).communicate()[0]

			if msg.is_direct:
				self.send(msg.frm, output.decode('unicode_escape'))
			else:
				self.send(msg.to, output.decode('unicode_escape'))

		except Exception as e:
			if msg.is_direct:
				self.send(msg.frm, 'Exception: %s' % e)
			else:
				self.send(msg.to, 'Exception: %s' % e)