import json

class JSONManager():

    def __init__(self, aContext):
        self.aContext = aContext

    def writeJSON(self, filename, data):
        file = self.aContext.get_resource(filename)
        with open(file, 'w') as outfile:  
            json.dump(data, outfile)

    def readJson(self, filename):
        file = self.aContext.get_resource(filename)
        with open(file) as json_file:
            data = json.load(json_file)
            return data

