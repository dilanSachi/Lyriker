from PorterStemmer import PorterStemmer
from NumberToWord import NumberToWord
import re

class WordNormalizer():

    def __init__(self):
        self.pStemmer = PorterStemmer()
        self.num2Word = NumberToWord()
        self.stopWords = ["i", "me", "my", "we", "the", "on", "and", "in", "to", "s", "t", "a", "an", "at", "of", "is", "or", "by", "it", "as", "be"]
        self.sOutput = []
        self.artistNames = []
        self.albumNames = []

    def convertNumbers(self, number):
        return self.num2Word.convert(number).split(" ")

    def removeStopWords(self, word):
        if(word in self.stopWords):
            return False
        else:
            return True
    
    def stemWord(self, word):
        return self.pStemmer.stem(word)

    def formatArtistName(self, name):
        name = name.strip()
        temp = re.sub(r'[\(\)\*\.\?\'\"\`\’]', '', name)
        formattednames = re.split(";|,|-|!|\r|\n|\s|{|}|[|]", temp)
        for formattedname in formattednames:
            self.artistNames.append(formattedname.lower())

    def formatAlbumName(self, name):
        name = name.strip()
        temp = re.sub(r'[\(\)\*\.\?\'\"\`\’]', '', name)
        formattednames = re.split(";|,|-|!|\r|\n|\s|{|}|[|]", temp)
        for formattedname in formattednames:
            """try:
                stemmedWord = self.stemWord(formattedname)
            except:
                stemmedWord = formattedname"""
            self.albumNames.append(formattedname.lower())

    def formatLine(self, words):
        words = words.strip()
        temp = re.sub(r'[\(\)\*\.\?\'\"\`\’]', '', words)
        formattedWords = re.split(";|,|-|!|\r|\n|\s|{|}|[|]", temp)
        #print(formattedWords)
        for word in formattedWords:
            if(len(word) >1):
                try:
                    num = int(word)
                    numWords = self.convertNumbers(num)
                    for numWord in numWords:
                        self.sOutput.append(numWord)
                        """try:
                            self.sOutput[numWord] = self.sOutput[numWord] + 1
                        except:
                            self.sOutput[numWord] = 1
                        #wordArr.append(numWord)"""
                except:
                    #stemmedWord = self.stemWord(word)
                    #if(self.removeStopWords(stemmedWord) and  stemmedWord not in wordArr):
                    if(self.removeStopWords(word)):
                        word = word.lower()
                        """try:
                            stemmedWord = self.stemWord(word)
                        except:
                            stemmedWord = word"""
                        self.sOutput.append(word)
                        """try:
                            self.sOutput[word] = self.sOutput[word] + 1
                        except:
                            self.sOutput[word] = 1
                        #wordArr.append(word)"""

    def normalizeLyrics(self, sInput):
        for parts in sInput:
            self.formatLine(parts)
        return(self.sOutput)

    def normalizeArtistNames(self, sInput):
        self.formatArtistName(sInput)
        return self.artistNames

    def normalizeAlbumNames(self, sInput):
        self.formatAlbumName(sInput)
        return self.albumNames
#w = WordNormalizer()
#w.normalize(["When ", "Johnny", " Jones was ", "serenading", " Mary\r\nHe sure ", "could", " quote a lot of poetry\r\nBut he'd much ", "rather", " tell 'er what he ", "learned", " in his speller\r\nWhen they both ", "attended", " ", "PS", " 33\r\n\r\n(A) you're adorable\r\n(B) you're so beautiful\r\n(C) you're a ", "cutie", " full of charms\r\n(D) you're a ", "darling", " and\r\n(E) you're exciting\r\n(F) you're a ", "feather", " in my arms\r\n\r\n(G) you look good to me\r\n(H) you're so heavenly\r\n(I) you're the one I idolize\r\n(J) we're like Jack and Jill\r\n(K) you're so kissable\r\n(L) is the love ", "light", " in your eyes\r\n\r\nM, N, O, P (you ", "could", " go on all day)\r\nQ ,R, S, T (alphabetically speaking, you're OK)\r\n\r\n(U) made my life complete\r\n(V) ", "means", " you're *awf'lly sweet*\r\nW, X, Y, Z\r\nIts fun to ", "wander", " through\r\nThe ", "alphabet", " with you\r\nTo tell (us what?) I mean (uh-huh?)\r\nTo tell you what you mean to me\r\n(We love you alphabetically)"])
    
