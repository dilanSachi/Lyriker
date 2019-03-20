from LetterDeleter import LetterDeleter
import json

class LetterDeleteFormatter():

    def __init__(self, aContext):
        self.aContext = aContext
        self.lDeleter = LetterDeleter()
        self.deletesDict = {}

    def readJson(self):
        file = self.aContext.get_resource('OriginalWords.json')
        with open(file) as json_file:
            words = json.load(json_file)
            return words

    def formatJSONDictionary(self, deletedWord, originalWord):
        try:
            self.deletesDict[deletedWord].append(originalWord)
        except:
            self.deletesDict[deletedWord] = []
            self.deletesDict[deletedWord].append(originalWord)

    def format(self):
        for key in self.readJson():
            self.lDeleter.edits = []
            deletedWords = self.lDeleter.delete(key, 2)
            for deletedWord in deletedWords:
                self.formatJSONDictionary(deletedWord, key)
        wordFile = self.aContext.get_resource('DeletedWords.json')
        with open(wordFile, 'w') as outfile:  
            json.dump(self.deletesDict, outfile)
        
        print(self.deletesDict)
            

    