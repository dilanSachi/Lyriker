from PorterStemmer import PorterStemmer
from NumberToWord import NumberToWord
import re

class WordNormalizer():

    def __init__(self, aContext):
        self.aContext = aContext
        self.pStemmer = PorterStemmer()
        self.num2Word = NumberToWord()
        self.stopWords = ["i", "me", "my", "we", "the", "on", "in", "to", "s", "t", "a", "an", "at", "of", "is", "or", "by", "it", "as", "be"]

    def convertNumbers(number):
        return self.num2Word.convert(number).split("")

    def removeStopWords(word):
        if(word in self.stopWords):
            return True
        else:
            return False
    
    def stemWord(word):
        return self.pStemmer.stem(word)

    def formatLine(words):
        wordArr = []
        words = words.strip()
        formattedWords = re.split(";|,|\r|\n|\s|{|}|[|]", words)
        for word in words:
            try:
                num = int(word)
                numWords = self.convertNumbers(num)
                for word in numWords:
                    wordArr.append(word)
            except:
                wordArr.append(word)

    def normalize(sInput):
        sOutput = []
        for parts in sInput:

    
    
