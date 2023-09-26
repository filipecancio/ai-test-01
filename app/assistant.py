from general_functions import  getJson

class Assistant():    
    def __init__(self):
        self.settings = getJson("/util/data/config.json")
        self.ASSISTANT_NAME = self.settings["assistant_name"]

    def doComand(self, command):
        if self.isCorrectAssitant(command[0]) and self.isValidCommand(command[1], command[2]):
            return f"executando {command[1]} sobre {command[2]}"
        else:
            return "Não entendi o que você disse"
        
    def isCorrectAssitant(self, name):
        return name == self.ASSISTANT_NAME
    
    def isValidCommand(self, action, target):
        for settings_action in self.settings["action"]:
            if settings_action["name"] == action:
                if target in settings_action["target"]:
                    return True
                
        return False