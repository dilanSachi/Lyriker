from SQLiteConnector import SQLiteConnector
from JsonDB import JsonDB
from Controller import Controller

class HistoryAnalyzer():

    def __init__(self, aContext, jsondb):
        self.jsondb = jsondb
        self.aContext = aContext

    def calcFavArtists(self):
        sqlt = SQLiteConnector(self.aContext)
        stmt = '''select * from searchhistory'''
        history = sqlt.readDB(stmt, [])
        print(history)
        searchedArtists = []
        searchedArtistsFrequency = []
        for song in history:
            try:
                ind = searchedArtists.index(song[1])
                searchedArtistsFrequency[ind] = searchedArtistsFrequency + song[2]
            except:
                searchedArtists.append(song[1])
                searchedArtistsFrequency.append(song[2])
        favArtists = []
        for i in range(6):
            if(len(searchedArtistsFrequency)==i):
                break
            ind = searchedArtistsFrequency.index(max(searchedArtistsFrequency))
            favArtists.append(searchedArtists[ind])
            searchedArtistsFrequency[ind] = 0

        return favArtists

    def getSongSuggestions(self, favArtists):
        cntlr = Controller(self.aContext)
        results = []
        i = 1
        for favArtist in favArtists:
            results = results + cntlr.processInput("artist", favArtist, self.jsondb)
            results = results[:4*i]
            i = i + 1
        print(results)
        songsData = cntlr.getSongsData(results, self.jsondb)
        return songsData


#also calculate fav songs in most searched albums too