from WordNormalizer import WordNormalizer
import json
from JSONManager import JSONManager

class JsonOriginalWordCreator():

    def __init__(self, aContext):
        self.aContext = aContext
        self.normalizer = WordNormalizer()
        self.wordArray = []
        self.wordDict = {}
        self.artistNameDict = {}
        self.jm = JSONManager(self.aContext)

    def getLyrics(self):
        data = self.jm.readJson('3.json')
        lyrics = []
        for song in data['Songs']:
            lyrics.append(song['Lyrics'])
        return lyrics

    def getArtistNames(self):
        data = self.jm.readJson('3.json')
        artists = []
        for song in data['Songs']:
            artists.append(song['Artist'])
        return artists

    #def getSongNames()

    def formatLyricDictionary(self, word, songNum):
    #def formatLyricDictionary(self, word, count, songNum):
        try:
            self.wordDict[word].append(songNum)
            #self.wordDict[word][0].append(songNum)
            #self.wordDict[word][1].append(count)
            
        except:
            self.wordDict[word] = []
            self.wordDict[word].append(songNum)
            #self.wordDict[word] = [[],[]]
            #self.wordDict[word][0].append(songNum)
            #self.wordDict[word][1].append(count)

    def formatArtistDictionary(self, name, songNum):
        try:
            self.artistNameDict[name].append(songNum)
        except:
            self.artistNameDict[name] = []
            self.artistNameDict[name].append(songNum)

    def formatLyrics(self):
        i = 1
        for lyric in self.getLyrics():
            self.normalizer.sOutput = []
            normalizedDict = self.normalizer.normalizeLyrics(lyric)
            for value in normalizedDict:
            #for key, value in normalizedDict.items():
                #self.formatLyricDictionary(key, value, i)
                self.formatLyricDictionary(value, i)
            i = i + 1
        self.jm.writeJSON('OriginalWords.json', self.wordDict)

    def formatArtistNames(self):
        i = 1
        for artist in self.getArtistNames():
            self.normalizer.artistNames = []
            artistNames = self.normalizer.normalizeArtistNames(artist)
            for artistName in artistNames:
                self.formatArtistDictionary(artistName, i)
            i = i + 1
        self.jm.writeJSON('OriginalArtistNames.json', self.artistNameDict)