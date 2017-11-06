<center><h1> Errbot plugin used in mcstn_bot</h1></center>

![bot screenshot](/images/unpackMalware.png)

Some plugins used on my Telegram Chat Bot.
They need to be used with [errbot](https://gitter.im/errbotio/errbot)

Youtube presentation fo the chatbot: https://www.youtube.com/watch?v=skXFNhBxIbI

## Configuration

The example configuration file config.conf. You need to put some API key inside this file, and path of your yara rules.

## Plugins

auto_beer			print a week end alert at Friday 18h.<br />
auto_bonjour		print bonjourMadame during the week and bonjourMademoiselle in the weekend.<br />
bitcoin				retrieve most famous cryptomoney values.<br />
giphy				print a random gif picture from giphy<br />
vt [hash]			check a hash on virustotal, and return all antivirus analysis<br />
malware	[URL]		made a malware analysis from a url, parse it through a malwares yara rules to identify it and try to uncrypt is configuration (if the sample is supported)<br />
					All the analysis scripts files are available in the addins folder. You can use [ratDecoders](https://github.com/kevthehermit/RATDecoders) scripts, but they are in python2, they need to be convert to python3 or you can use a python3 script to call them like i have do (Quite dirty). 
unpack [URL] 		try to unpack a sample, parse it through a packer yara rules to identify it (Only UPX is actualy supported)<br />
yara [URL]			yara check<br />
shodan [URL]		shodan search<br />
ip [IP]				ip info<br />
urlquery [URL]		search pattern in urlquery gse<br />
gse_find [URL]		search pattern in google gse<br />
unshorten [URL]		unshorten a url<br />