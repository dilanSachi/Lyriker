from LetterDeleter import LetterDeleter
import json
from JSONManager import JSONManager

class LetterDeleteFormatter():

    def __init__(self, aContext):
        self.aContext = aContext
        self.lDeleter = LetterDeleter()
        self.deletesDict = {"words":[]}
        for i in range(27):
            self.deletesDict["words"].append({"words":[{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{}]})
        self.deletesDict["words"].append({})

    def formatJSONDictionary(self, deletedWord, originalWord):
        if(96 < ord(deletedWord[0]) < 123):
            ind1 = ord(deletedWord[0]) - 97
        else:
            ind1 = 26
        if(len(deletedWord) > 1):
            if(96 < ord(deletedWord[1]) < 123):
                ind2 = ord(deletedWord[1]) - 97
            else:
                ind2 = -1
            try:
                self.deletesDict["words"][ind1]["words"][ind2][deletedWord].append(originalWord)
            except:
                self.deletesDict["words"][ind1]["words"][ind2][deletedWord] = []
                self.deletesDict["words"][ind1]["words"][ind2][deletedWord].append(originalWord)
        else:
            try:
                self.deletesDict["words"][27][deletedWord].append(originalWord)
            except:
                self.deletesDict["words"][27][deletedWord] = []
                self.deletesDict["words"][27][deletedWord].append(originalWord)
        #print(len(deletedWord))
        


        """
        try:
            self.deletesDict[ind][len(deletedWord)][deletedWord].append(originalWord)
        except:
            try:
                self.deletesDict[ind][len(deletedWord)][deletedWord] = []
                self.deletesDict[ind][len(deletedWord)][deletedWord].append(originalWord)
            except:
                self.deletesDict[ind][len(deletedWord)] = {}
                self.deletesDict[ind][len(deletedWord)][deletedWord] = []
                self.deletesDict[ind][len(deletedWord)][deletedWord].append(originalWord)
"""

    def format(self):
        jm = JSONManager(self.aContext)
        for key in jm.readJson('OriginalWords.json'):
            self.lDeleter.edits = []
            deletedWords = self.lDeleter.delete(key, 2)
            for deletedWord in deletedWords:
                self.formatJSONDictionary(deletedWord, key)
        jm.writeJSON('DeletedWords.json', self.deletesDict)
        #print(self.deletesDict)
            

    