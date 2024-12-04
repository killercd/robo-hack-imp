from app.robohack.mod.utils.utils import *

class SqlMapMod():
    
    def __init__(self, 
                target, 
                requestfile,
                postdata,
                cookie,
                random_agent,
                proxy,
                tor,
                forcessl,
                risk,
                level,
                batch
                ):
        
        self.target = target
        self.requestfile = requestfile
        self.postdata = postdata
        self.cookie = cookie
        self.random_agent = random_agent
        self.proxy = proxy
        self.tor = tor
        self.forcessl = forcessl
        self.risk = risk
        self.level = level
        self.batch = batch

    def generate(self):
        
        g_command = f"sqlmap"
        if self.target:
            g_command = f"{g_command} -u '{self.target}'"
        elif self.requestfile:
            g_command = f"{g_command} -r '{self.requestfile}'"

        if self.postdata:
            g_command = f"{g_command} --data='{self.postdata}'"
        
        if self.cookie:
            g_command = f"{g_command} --cookie='{self.cookie}'"
        
        if self.random_agent:
            g_command = f"{g_command} --random_agent"
        
        if self.proxy:
            g_command = f"{g_command} --proxy='{self.proxy}'"
        
        if self.tor:
            g_command = f"{g_command} --tor"

        if self.forcessl:
            g_command = f"{g_command} --forcessl"

        if self.risk:
            g_command = f"{g_command} --risk={self.risk}"

        if self.level:
            g_command = f"{g_command} --level={self.level}"

        if self.batch:
            g_command = f"{g_command} --batch"

        data = {
            "target": nte(self.target),
            "requestfile": nte(self.requestfile),
            "postdata": nte(self.postdata),
            "cookie": nte(self.cookie),
            "random_agent": nte(self.random_agent),
            "proxy": nte(self.proxy),
            "tor": nte(self.tor),
            "forcessl": nte(self.forcessl),
            "risk": nte(self.risk),
            "level": nte(self.level),
            "batch": nte(self.batch),
            "command": g_command
        }
        return data


    @staticmethod
    def empty_data():
        return  {
            "target": "",
            "requestfile": "",
            "postdata": "",
            "cookie": "",
            "random_agent": "",
            "proxy": "",
            "tor": "",
            "forcessl": "",
            "risk": "",
            "level": "",
            "batch": "",
            "command": ""
        }
