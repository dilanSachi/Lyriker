import json
import re
from LetterDeleter import LetterDeleter
from SQLiteConnector import SQLiteConnector

class SpellCorrector():
    def __init__(self, aContext):
        self.aContext = aContext
        self.wordCollection = []
        self.wordConnections = []

    def readJson(self):
        file = self.aContext.get_resource('2.json')
        with open(file) as json_file:
            songs = json.load(json_file)
            i = 0
            lyrics = []
            for p in songs['Songs']:
                lyrics.append(p['Lyrics'])
                i = i + 1
            return lyrics

    def getSongData(self, song):
        file = self.aContext.get_resource('4.json')
        with open(file) as json_file:
        #with open('4.json') as json_file:
            songs = json.load(json_file)
            return songs['Songs'][song]
        json_file.close()

    def formatLyrics(self, lyrics):
        ld = LetterDeleter()

        song = 1

        for i in lyrics:
            for wordSet in i:
                wordSet = wordSet.strip()
                formattedWords = re.split(";|,|\r|\n|\s|{|}|[|]", wordSet)
                for formattedWord in formattedWords:
                    if(formattedWord != " "):
                        try:
                            formattedWord = formattedWord.lower()
                            originalWordIndex = self.wordCollection.index([formattedWord])
                        except:
                            originalWordIndex = -1
                        if (originalWordIndex == -1):
                            self.wordCollection.append([formattedWord])
                            originalWordIndex = len(self.wordCollection) - 1
                            self.wordConnections.append([song, originalWordIndex+1, originalWordIndex+1])
                        else:
                            self.wordConnections.append([song, originalWordIndex+1, originalWordIndex+1])
                        ld.edits = []
                        deletedWords = ld.delete(formattedWord, 2)
                        for deletedWord in deletedWords:
                            try:
                                ind = self.wordCollection.index([deletedWord])
                            except:
                                ind = -1
                            if(ind == -1):
                                self.wordCollection.append([deletedWord])
                                self.wordConnections.append([song, originalWordIndex+1, len(self.wordCollection)])
                            else:
                                self.wordConnections.append([song, originalWordIndex+1, ind+1])
            song = song + 1
        print(self.wordCollection)
        print(self.wordConnections)
        #print(len(self.wordCollection))
        #print(len(self.wordConnections))

    def saveToDB(self):
        wordsStatement = ''' INSERT INTO words(word) VALUES(?)'''
        connectionsStatement = ''' INSERT INTO connections(song, originalWordIndex, wordIndex) VALUES(?, ?, ?)'''
        sqltconn = SQLiteConnector(self.aContext)
        sqltconn.createDB()
        sqltconn.executeMany(wordsStatement, self.wordCollection)
        sqltconn.executeMany(connectionsStatement, self.wordConnections)

        #sqltconn.joinDB()

    def search(self, term):
        sqltconn = SQLiteConnector(self.aContext)
        rows = sqltconn.joinDB(term)
        originalWords = []
        songs = []
        print(rows)
        for row in rows:
            originalWords.append(row[2])
            songs.append(row[1])
        #print(originalWords, songs)
        return originalWords,songs
        #return songs
#w = SpellCorrector()
#w.formatLyrics(w.readJson())
#w.saveToDB()
#w.search("whe")
#w.search("Jonny")
#print(w.getSongData(2))