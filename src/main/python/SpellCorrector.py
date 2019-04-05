from LetterDeleter import LetterDeleter
import json
from JsonDB import JsonDB

class SpellCorrector():

    def __init__(self, jsondb):
        self.letDelter = LetterDeleter()
        self.jsondb = jsondb

    def checkMatches(self, uType, word):

        if(uType == "lyric"):
            deletedDB = self.jsondb.getDeletedWordsDB()
        elif(uType == "artist"):
            deletedDB = self.jsondb.getDeletedNamesDB()

        matchingWords = []
        self.letDelter.edits = []
        deletedWords = self.letDelter.delete(word, 2)
        for deletedWord in deletedWords:
            try:
                if(len(deletedWord)>1):
                    if(96< ord(deletedWord[0]) < 123):
                        ind1 = ord(deletedWord[0])-97
                    else:
                        ind1 = 26
                    if(96< ord(deletedWord[1]) < 123):
                        ind2 = ord(deletedWord[1])-97
                    else:
                        ind2 = -1
                    matchingWords.append(deletedDB["words"][ind1]["words"][ind2][deletedWord])
                else:
                    matchingWords.append(deletedDB["words"][27][deletedWord])
            except:
                #print("Couldn't find",deletedWord)
                a = True
        return matchingWords
    
    def getMostFrequentWords(self, matchingWords):
        correctWords =[]
        words = []
        wordFrequency = []
        for wordList in matchingWords:
            for word in wordList:
                try:
                    ind = words.index(word)
                    wordFrequency[ind] = wordFrequency[ind] + 1
                except:
                    words.append(word)
                    wordFrequency.append(1)
        #print("freq",wordFrequency)
        #print("word",words)
        for i in range(6):
            if(len(wordFrequency)==i):
                break
            ind = wordFrequency.index(max(wordFrequency))
            correctWords.append(words[ind])
            wordFrequency[ind] = 0
        return correctWords
