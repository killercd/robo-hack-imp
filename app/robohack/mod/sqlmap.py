from app.robohack.mod.utils.utils import *

class SqlMapMod():
    
    def __init__(self, 
                target, 
                request):
        
        self.target = target
        self.request = request
        

    def generate(self):
        
        g_command = f"sqlmap "
        if self.target:
            g_command = f"{g_command} -u {self.target}"
        elif self.request:
            g_command = f"{g_command} -r '{self.request}'"
        

        data = {
            "target": nte(self.target),
            "request": nte(self.request),
            "command": g_command
        }
        return data


    @staticmethod
    def empty_data():
        return {"target": "", "request": ""}