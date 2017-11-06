import os, requests, string, re, sys
from errbot import BotPlugin, botcmd, arg_botcmd

class Unshorten(BotPlugin):

    @arg_botcmd('url', type=str)
    def unshorten(self, msg, url=None):
        try:
            
            headers = {
                "User-Agent" : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                "Accept-Encoding": "none",
                "Accept-Language": "en-US,en;q=0.8",
                "Connection": "keep-alive"
                }

            response = requests.get('https://unshorten.me/raw/' + url, headers=headers)
            data = response.text
            data = re.search("(?P<url>https?://[^\s]+)", data).group("url")
            data = re.sub('http', 'hxxp', data)

            return(data)

        except Exception as e:

            self._bot.telegram.sendMessage(chat_id="289979691", text="Exception : " + str(e) + ". Line: " + format(sys.exc_info()[-1].tb_lineno))
    
        return data 
