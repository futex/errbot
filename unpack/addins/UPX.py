#!/usr/bin/python
import subprocess
from config import BOT_DATA_DIR

def unpack(maliciousFile):

	try:
		subprocess.call("(upx -d %s)" %maliciousFile, shell=True)
		return maliciousFile
	except Exception as e:
		return None

