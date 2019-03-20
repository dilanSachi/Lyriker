import json

class JSONManager():

    def __init__(self, aContext):
        self.aContext = aContext

    def writeJSON(self):
        file = self.aContext.get_resource('OriginalWords.json')
        with open(file) as json_file:
            data = json.load(json_file)
            print(data['pukgedda'])

