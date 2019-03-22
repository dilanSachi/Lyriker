from LetterDeleter import LetterDeleter
import json

class LetterDeleteFormatter():

    def __init__(self, aContext):
        self.aContext = aContext
        self.lDeleter = LetterDeleter()
        temp = {"words":[{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{}]}
        self.deletesDict = {"words":[]}
        for i in range(27):
            self.deletesDict["words"].append({"words":[{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{}]})
        self.deletesDict["words"].append({})
        self.alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

    def readJson(self):
        file = self.aContext.get_resource('OriginalWords.json')
        with open(file) as json_file:
            words = json.load(json_file)
            return words

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
        for key in self.readJson():
            self.lDeleter.edits = []
            deletedWords = self.lDeleter.delete(key, 2)
            for deletedWord in deletedWords:
                self.formatJSONDictionary(deletedWord, key)
        wordFile = self.aContext.get_resource('DeletedWords.json')
        with open(wordFile, 'w') as outfile:  
            json.dump(self.deletesDict, outfile)
        
        #print(self.deletesDict)
            

    