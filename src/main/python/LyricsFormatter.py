from WordNormalizer import WordNormalizer
import json

class LyricsFormatter():

    def __init__(self, aContext):
        self.aContext = aContext
        self.normalizer = WordNormalizer(self.aContext)
        self.wordArray = []
        self.wordDict = {}

    def readJson(self):
        file = self.aContext.get_resource('3.json')
        with open(file) as json_file:
            songs = json.load(json_file)
            i = 0
            lyrics = []
            for p in songs['Songs']:
                lyrics.append(p['Lyrics'])
                i = i + 1
            return lyrics

    def formatJSONDictionary(self, word, count, songNum):
        try:
            self.wordDict[word][songNum] = count
        except:
            self.wordDict[word] = {}
            self.wordDict[word][songNum] = count


    def formatLyrics(self):
        i = 1
        for lyric in self.readJson():
            self.normalizer.sOutput = {}
            normalizedDict = self.normalizer.normalize(lyric)
            for key, value in normalizedDict.items():
                self.formatJSONDictionary(key, value, i)
            i = i + 1
        wordFile = self.aContext.get_resource('OriginalWords.json')
        with open(wordFile, 'w') as outfile:  
            json.dump(self.wordDict, outfile)
