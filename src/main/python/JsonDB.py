import json
from JSONManager import JSONManager

class JsonDB():

    def __init__(self, aContext):
        self.aContext = aContext
        self.deletedWordsDB = ""
        self.originalWordsDB = ""

    def loadDeletedWordsDB(self):
        jsonM = JSONManager(self.aContext)
        self.deletedWordsDB = jsonM.readJson('DeletedWords.json')

    def loadOriginalWordsDB(self):
        jsonM = JSONManager(self.aContext)
        self.originalWordsDB = jsonM.readJson('OriginalWords.json')

    def getDeletedWordsDB(self):
        return self.deletedWordsDB

    def getOriginalWordsDB(self):
        return self.originalWordsDB
        