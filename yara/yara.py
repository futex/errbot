from errbot import BotPlugin, botcmd
import subprocess
import configparser
import ast

class yara(BotPlugin):

    @botcmd
    def yara(self, msg, args):

        Config = configparser.ConfigParser()
        Config.read("./config.conf")
        YARA_PATH=ast.literal_eval(Config.get("YARA", "YARA_PATH"))
        YARA_RULES_PATH=ast.literal_eval(Config.get("YARA", "YARA_RULES_PATH"))

        filepath = "/tmp/mal"

        draft_dir = "/tmp/tmp_malw"

        try:

            remote_file = args[0]

            urllib.urlretrieve (remote_file, filepath)

            output = subprocess.Popen([YARA_PATH, "-w", YARA_RULES_PATH + "rules/*", filepath], stdout=subprocess.PIPE).communicate()[0]
    
            value = output.split(' ')[0]
            
            if value == "":
                value = "Unknown sample"

        except Exception as e:
            if msg.is_direct:
                self.send(msg.frm, 'Exception: %s' % e)
            else:
                self.send(msg.to, 'Exception: %s' % e)

        if msg.is_direct:
            self.send(msg.frm, value)
        else:
            self.send(msg.to, value)
