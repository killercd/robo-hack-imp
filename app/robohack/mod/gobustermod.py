from app.robohack.mod.utils.utils import *

class GobusterMod():
    def __init__(self, target, 
                wordlist,
                cookies,
                extension,
                nossl):
        
        self.target = target
        self.wordlist = wordlist
        self.cookies = cookies
        self.extension = extension
        self.nossl = nossl

    def generate(self):
        
        g_command = f"gobuster dir -u {self.target}"
        if self.wordlist:
            g_command = f"{g_command} -w {self.wordlist}"
        if self.cookies:
            g_command = f"{g_command} -c '{self.cookies}'"
        if self.extension:
            g_command = f"{g_command} -x {self.extension}"
        if self.nossl and self.nossl=="enabled":
            g_command = f"{g_command} -k"

        data = {
            "target": nte(self.target),
            "wordlist": nte(self.wordlist),
            "cookies": nte(self.cookies),
            "extension": nte(self.extension),
            "nossl": self.nossl,
            "command": g_command
        }
        return data
        

    @staticmethod
    def empty_data():
        return {"target": "", 
                "wordlist": "", 
                "cookies": "", 
                "cookies": "", 
                "extension": "",
                "nossl": "disabled"}