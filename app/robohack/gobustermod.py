class GobusterMod():
    def __init__(self, target, 
                wordlist,
                cookies,
                extension,
                no_tsl_validation):
        
        self.target = target
        self.wordlist = wordlist
        self.cookies = cookies
        self.extension = extension
        self.no_tsl_validation = no_tsl_validation

    def generates(self):
        
        g_command = f"gobuster dir -u {self.target}"
        if self.wordlist:
            g_command = f"{g_command} -w {self.wordlist}"
        if self.cookies:
            g_command = f"{g_command} -c '{self.cookies}'"
        if self.extension:
            g_command = f"{g_command} -x {self.extension}"
        if self.no_tsl_validation and self.no_tsl_validation=="enabled":
            g_command = f"{g_command} -k"
        return g_command