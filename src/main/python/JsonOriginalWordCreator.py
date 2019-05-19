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
        self.albumNameDict = {}
        self.jm = JSONManager(self.aContext)

    def getDataFromFile(self, typ):
        data = self.jm.readJson('5.json')
        temp = []
        for song in data['Songs']:
            temp.append(song[typ])
        return temp

    def formatDictionary(self, word, songNum, dictionary):
        try:
            dictionary[word].append(songNum)
        except:
            dictionary[word] = []
            dictionary[word].append(songNum)

    def formatLyrics(self):
        i = 1
        for lyric in self.getDataFromFile('Lyrics'):
            self.normalizer.sOutput = []
            normalizedDict = self.normalizer.normalizeLyrics(lyric)
            for value in normalizedDict:
            #for key, value in normalizedDict.items():
                #self.formatLyricDictionary(key, value, i)
                self.formatDictionary(value, i, self.wordDict)
            i = i + 1
        self.jm.writeJSON('OriginalWords.json', self.wordDict)

    def formatArtistNames(self):
        i = 1
        for artist in self.getDataFromFile('Artist'):
            self.normalizer.artistNames = []
            artistNames = self.normalizer.normalizeArtistNames(artist)
            for artistName in artistNames:
                self.formatDictionary(artistName, i, self.artistNameDict)
            i = i + 1
        self.jm.writeJSON('OriginalArtistNames.json', self.artistNameDict)

    def formatAlbumNames(self):
        i = 1
        for album in self.getDataFromFile('Album'):
            self.normalizer.albumNames = []
            albumNames = self.normalizer.normalizeAlbumNames(album)
            for albumName in albumNames:
                self.formatDictionary(albumName, i, self.albumNameDict)
            i = i + 1
        self.jm.writeJSON('OriginalAlbumNames.json', self.albumNameDict)