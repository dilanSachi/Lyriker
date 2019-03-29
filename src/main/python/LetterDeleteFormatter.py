from LetterDeleter import LetterDeleter
import json
from JSONManager import JSONManager

class LetterDeleteFormatter():

    def __init__(self, aContext):
        self.aContext = aContext
        self.lDeleter = LetterDeleter()
        self.wordDeletesDict = {"words":[]}
        self.nameDeletesDict = {}
        for i in range(27):
            self.wordDeletesDict["words"].append({"words":[{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{}]})
        self.wordDeletesDict["words"].append({})

    def formatWordDict(self, deletedWord, originalWord):
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
                self.wordDeletesDict["words"][ind1]["words"][ind2][deletedWord].append(originalWord)
            except:
                self.wordDeletesDict["words"][ind1]["words"][ind2][deletedWord] = []
                self.wordDeletesDict["words"][ind1]["words"][ind2][deletedWord].append(originalWord)
        else:
            try:
                self.wordDeletesDict["words"][27][deletedWord].append(originalWord)
            except:
                self.wordDeletesDict["words"][27][deletedWord] = []
                self.wordDeletesDict["words"][27][deletedWord].append(originalWord)
    
    def formatArtistNamesDict(self, deletedName, originalName):
        try:
            self.nameDeletesDict[deletedName].append(originalName)
        except:
            self.nameDeletesDict[deletedName] = []
            self.nameDeletesDict[deletedName].append(originalName)


    def formatWords(self):
        jm = JSONManager(self.aContext)
        for key in jm.readJson('OriginalWords.json'):
            self.lDeleter.edits = []
            deletedWords = self.lDeleter.delete(key, 2)
            for deletedWord in deletedWords:
                self.formatWordDict(deletedWord, key)
        jm.writeJSON('DeletedWords.json', self.wordDeletesDict)
        #print(self.deletesDict)

    def formatArtistNames(self):
        jm = JSONManager(self.aContext)
        for key in jm.readJson('OriginalArtistNames.json'):
            self.lDeleter.edits = []
            deletedWords = self.lDeleter.delete(key, 2)
            for deletedWord in deletedWords:
                self.formatArtistNamesDict(deletedWord, key)
        jm.writeJSON('DeletedArtistNames.json', self.nameDeletesDict)
            

    