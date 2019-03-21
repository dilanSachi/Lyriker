from LetterDeleter import LetterDeleter
import json

class LetterDeleteFormatter():

    def __init__(self, aContext):
        self.aContext = aContext
        self.lDeleter = LetterDeleter()
        self.deletesDict = [{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{}]
        self.alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

    def readJson(self):
        file = self.aContext.get_resource('OriginalWords.json')
        with open(file) as json_file:
            words = json.load(json_file)
            return words

    def formatJSONDictionary(self, deletedWord, originalWord):
        #print(len(deletedWord))
        try:
            ind = self.alphabet.index(deletedWord[0])
        except:
            ind = 26
        try:
            self.deletesDict[ind][deletedWord].append(originalWord)
        except:
            self.deletesDict[ind][deletedWord] = []
            self.deletesDict[ind][deletedWord].append(originalWord)

    def format(self):
        for key in self.readJson():
            self.lDeleter.edits = []
            deletedWords = self.lDeleter.delete(key, 2)
            for deletedWord in deletedWords:
                self.formatJSONDictionary(deletedWord, key)
        for i in range(27):
            if(i == 26):
                wordFile = self.aContext.get_resource('DeletedWordsOther.json')
            else:
                wordFile = self.aContext.get_resource('DeletedWords' +self.alphabet[i] + '.json')
            with open(wordFile, 'w') as outfile:  
                json.dump(self.deletesDict[i], outfile)
        
        print(self.deletesDict)
            

    