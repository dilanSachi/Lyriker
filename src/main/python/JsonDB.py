import json
from JSONManager import JSONManager

class JsonDB():

    def __init__(self, aContext):
        self.aContext = aContext
        self.jsonM = JSONManager(self.aContext)
        self.deletedWordsDB = ""
        self.originalWordsDB = ""
        self.songsDB = ""
        self.originalNamesDB= ""
        self.deletedNamesDB = ""
        self.originalAlbumsDB = ""
        self.deletedAlbumsDB = ""

    def loadDeletedWordsDB(self):
        self.deletedWordsDB = self.jsonM.readJson('DeletedWords.json')

    def loadOriginalWordsDB(self):
        self.originalWordsDB = self.jsonM.readJson('OriginalWords.json')

    def loadSongsDB(self):
        self.songsDB = self.jsonM.readJson('5.json')

    def loadOriginalNamesDB(self):
        self.originalNamesDB = self.jsonM.readJson('OriginalArtistNames.json')

    def loadDeletedNamesDB(self):
        self.deletedNamesDB = self.jsonM.readJson('DeletedArtistNames.json')

    def loadDeletedAlbumsDB(self):
        self.deletedAlbumsDB = self.jsonM.readJson('DeletedAlbumNames.json')

    def loadOriginalAlbumsDB(self):
        self.originalAlbumsDB = self.jsonM.readJson('OriginalAlbumNames.json')

    def getDeletedAlbumsDB(self):
        return self.deletedAlbumsDB

    def getOriginalAlbumsDB(self):
        return self.originalAlbumsDB

    def getDeletedWordsDB(self):
        return self.deletedWordsDB

    def getOriginalWordsDB(self):
        return self.originalWordsDB

    def getSongsDB(self):
        return self.songsDB

    def getOriginalNamesDB(self):
        return self.originalNamesDB

    def getDeletedNamesDB(self):
        return self.deletedNamesDB
        