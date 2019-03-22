from LetterDeleter import LetterDeleter
import json
import time

class SpellCorrectorNew():

    def __init__(self, aContext):
        self.aContext = aContext
        self.letDelter = LetterDeleter()
        self.matchingWords = []
        self.file = self.aContext.get_resource('DeletedWords.json')
        with open(self.file) as json_file:
            self.deletedDB = json.load(json_file)
        self.correctWords = []

    def checkMatchingWords(self, word):
        deletedWords = self.letDelter.delete(word, 2)
        start = time.time()
        for deletedWord in deletedWords:
            if(len(deletedWord)>1):
                if(96< ord(deletedWord[0]) < 123):
                    ind1 = ord(deletedWord[0])-97
                else:
                    ind1 = 26
                if(96< ord(deletedWord[1]) < 123):
                    ind2 = ord(deletedWord[1])-97
                else:
                    ind2 = -1
                self.matchingWords.append(self.deletedDB["words"][ind1]["words"][ind2][deletedWord])
            else:
                self.matchingWords.append(self.deletedDB["words"][27][deletedWord])
            #deletedDB["words"][ind][deletedWord]
            #deletedDB[ind][str(len(deletedWord))][deletedWord]
            #deletedDB[str(len(deletedWord))][deletedWord]
        end = time.time()
    
    def getMostRelevantWords(self):
        words = []
        wordFrequency = []
        start = time.time()
        for wordList in self.matchingWords:
            for word in wordList:
                try:
                    ind = words.index(word)
                    wordFrequency[ind] = wordFrequency[ind] + 1
                except:
                    words.append(word)
                    wordFrequency.append(1)
        #print("freq",wordFrequency)
        #print("word",words)
        for i in range(5):
            if(len(wordFrequency)==i):
                break
            ind = wordFrequency.index(max(wordFrequency))
            self.correctWords.append(words[ind])
            wordFrequency[ind] = 0
        end = time.time()
        return self.correctWords