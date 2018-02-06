from errbot import BotPlugin, botcmd, arg_botcmd
#from os import path, mkdir, walk
import os
import subprocess
import socks
import socket
import requests
import configparser
import ast
import hashlib
import re
import sys
import importlib

class unpack(BotPlugin):

	def activate(self):
		super().activate()
		self.malw = self.get_plugin('malware').malware

	#Print message to chat
	def printMessage(self, msg, message):
		if msg.is_direct:
			self.send(msg.frm, message)
		else:
			self.send(msg.to,message)

	#Load all plugins from addin directory
	def load_plugins(self,msg):

		try:
			pysearchre = re.compile('.py$', re.IGNORECASE)
			pluginfiles = filter(pysearchre.search,
		                           os.listdir(os.path.join(os.path.dirname(__file__),
		                                                 'addins')))
			form_module = lambda fp: '.' + os.path.splitext(fp)[0]
			plugins = map(form_module, pluginfiles)

			importlib.import_module('addins')
			modules = []

			for plugin in plugins:

				if not plugin.startswith('__'):
					modules.append(importlib.import_module(plugin, package="addins"))
		
		except Exception as e:
			self.printMessage(msg, "Exception : " + str(e) + ". Line: " + format(sys.exc_info()[-1].tb_lineno))

		return modules

	#Scan YARA
	def yarascan(self, msg, maliciousFile):

		Config = configparser.ConfigParser()
		Config.read("./config.conf")
		YARA_PATH=ast.literal_eval(Config.get("YARA", "YARA_PATH"))
		YARA_RULES_PATH=ast.literal_eval(Config.get("YARA", "YARA_RULES_PATH"))
		YARA_PACKERS_RULES=ast.literal_eval(Config.get("YARA", "YARA_PACKERS_RULES"))
			
		output = str(subprocess.Popen([YARA_PATH, "-r", YARA_RULES_PATH + YARA_PACKERS_RULES, maliciousFile], stdout=subprocess.PIPE).communicate()[0].decode('unicode_escape'))
		hashmd5 = hashlib.md5(open(maliciousFile, 'rb').read()).hexdigest()
		value = output.split(' ')[0]

		if value == "":
			value = "Unknown sample"

		return value, hashmd5

	#Download the sample through TOR
	def download (self, msg, filepath, sample):
			
			try:

				socks.setdefaultproxy(proxy_type=socks.PROXY_TYPE_SOCKS5, addr="127.0.0.1", port=9050)

				r = requests.get(sample, stream=True)

				if r.status_code == 200:
					with open(filepath, 'wb') as f:
						for chunk in r.iter_content(1024):
							f.write(chunk)
					return True
				
				else:
					self.printMessage(msg, "Failed to retreive the sample, HTTP code: " + str(r.status_code))
					return False

			except socket.timeout as e:
				self.printMessage(msg, "Exception socket.timeout:  " + str(e) + ". Line: " + format(sys.exc_info()[-1].tb_lineno) )
				return False

			except socket.error as e:
				self.printMessage(msg, "Exception socket.error:  " + str(e) + ". Line: " + format(sys.exc_info()[-1].tb_lineno) )
				return False
			
			except requests.ConnectTimeout as e:
				self.printMessage(msg, "Exception  ConnectTimeout:  " + str(e) + ". Line: " + format(sys.exc_info()[-1].tb_lineno) )
				return False

	'''def unpackUPX(self, msg, maliciousFile):

		try:
			subprocess.call("(upx -d %s)" %maliciousFile, shell=True)
			return maliciousFile
		except Exception as e:
			self.printMessage(msg, 'UPX Error {0}'.format(e))
			return None'''

	@arg_botcmd('sample', type=str)
	def unpack(self, msg, sample=None):

		filepath = "/tmp/mal"
    
		draft_dir = "/tmp/tmp_malw"

		#Create tempory folder for the downloading malwares
		if not os.path.exists(draft_dir):
			os.makedirs(draft_dir)

		#The plugins folder is call addin, because plugins if already use and make an error in errbot
		if not os.path.exists( os.path.dirname(__file__) + '/addins'):
			os.makedirs(os.path.dirname(__file__) + '/addins')
		else:
			mod = self.load_plugins(msg)

		#If the file come from Internet
		if "http" in sample :
			if not self.download(msg, filepath, sample):
				return False

		#If the file must be uploaded
		else:

			filepath = sample

		value, hashmd5 = self.yarascan(msg, filepath)

		self.printMessage(msg, "Packer: " + value + ", MD5: " + hashmd5)


		for module in mod:
				
			if value.lower() in module.__name__ .lower():

				filepath = module.unpack(filepath)

				if filepath is not None:

					self.printMessage(msg, "Unpacked sample: ")
					self.send_stream_request(msg.frm, open(filepath, 'rb'), name='unpacked.exe', size=os.path.getsize(filepath), stream_type='document')
			else:
				self.printMessage(msg, "Unknown packer.")

		'''if value.lower() == "upx":
			filepath = self.unpackUPX(msg, filepath)

			if filepath is not None:
				self.printMessage(msg, "Unpacked sample: ")
				self.send_stream_request(msg.frm, open(filepath, 'rb'), name='unpacked.exe', size=os.path.getsize(filepath), stream_type='document')
		else:
			self.printMessage(msg, "Unknown packer.")'''

		self.malw(msg, filepath)


