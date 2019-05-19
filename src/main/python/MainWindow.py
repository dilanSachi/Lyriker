from fbs_runtime.application_context import ApplicationContext
from PyQt5.QtWidgets import QMainWindow, QMessageBox
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from LetterDeleter import LetterDeleter
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QAction
from PyQt5.QtCore import pyqtSlot
import sys
from MainWindowUI import Ui_Lyriker
from SQLiteConnector import SQLiteConnector
import sqlite3
from JsonDB import JsonDB
from HistoryAnalyzer import HistoryAnalyzer
from Controller import Controller

class MainWindow(ApplicationContext):


    def __init__(self, lyrikerWindow, check):
        super().__init__()

        self.lyrikerWindow = lyrikerWindow

        self.songsData = []
        self.counter = 0
        self.totSongs = []
        self.controller = Controller(self)

        self.ui = Ui_Lyriker()
        self.ui.setupUi(self.lyrikerWindow)

        self.loadJsonFiles()
        self.catchSearchBtnClk()

        self.lyrikerWindow.show()
        #self.ui.show()

        #self.qMainWindow.show()
        if(check == False):
          sys.exit(self.app.exec_())

    def loadJsonFiles(self):
        self.jsondb = JsonDB(self)
        self.jsondb.loadDeletedWordsDB()
        self.jsondb.loadOriginalWordsDB()
        self.jsondb.loadSongsDB()
        self.jsondb.loadOriginalNamesDB()
        self.jsondb.loadDeletedNamesDB()
        self.jsondb.loadOriginalAlbumsDB()
        self.jsondb.loadDeletedAlbumsDB()

    def catchSearchBtnClk(self):
        self.ui.btnLyricSearch.clicked.connect(self.searchByLyric)
        self.ui.btnArtistSearch.clicked.connect(self.searchByArtist)
        self.ui.btnAlbumSearch.clicked.connect(self.searchByAlbum)
        self.ui.btnBrowseSongs.clicked.connect(self.browseSongs)
        self.ui.btnViewSuggestions.clicked.connect(self.displaySuggestions)

    def browseSongs(self):
        print("browse songs")
        self.clearResults()
        total = len(self.jsondb.getSongsDB()['Songs'])
        if(self.totSongs == []):
            for i in range(total):
                self.totSongs.append(i + 1)
        results = []
        self.counter = 0
        for i in range(self.counter, self.counter+15):
            results.append(self.totSongs[i])
        self.counter += 15
        self.songsData = self.controller.getSongsData(results, self.jsondb)
        try:
            self.ui.resultListWidget.itemClicked.disconnect(self.displayNextSongs)
        except:
            print()
        self.displayResults()
        self.ui.resultListWidget.addItem("Next")
        self.ui.resultListWidget.itemClicked.connect(self.displayNextSongs)
        
    def displayNextSongs(self, item):
        print('inside')
        row = self.ui.resultListWidget.row(item)
        print(row)
        if(row == 15):
            print('next clckd')
            results = []
            for i in range(self.counter, self.counter+15):
                results.append(self.totSongs[i])
            self.counter += 15
            self.songsData = self.controller.getSongsData(results, self.jsondb)
            print(results)
            self.ui.resultListWidget.itemClicked.disconnect(self.displayNextSongs)
            #print(self.songsData)
            self.displayResults()
            self.ui.resultListWidget.addItem("Next")
            self.ui.resultListWidget.itemClicked.connect(self.displayNextSongs)
        else:
            self.processBrowsingResults(item)

    def processBrowsingResults(self, item):
        print('XXXXXXXXXXXXXXXXXXXXXX')
        row = self.ui.resultListWidget.row(item)
        self.saveToSearchHistory(self.songsData[row]['Title'], self.songsData[row]['Artist'])
        self.clearResults()
        self.ui.resultListWidget.itemClicked.disconnect(self.displayNextSongs)
        self.displayLyrics(self.songsData[row])

    def processResults(self, item):
        print('BBBBBBBBBBBBBBBBBBBBBBBB')
        row = self.ui.resultListWidget.row(item)
        self.saveToSearchHistory(self.songsData[row]['Title'], self.songsData[row]['Artist'])
        self.clearResults()
        self.ui.resultListWidget.itemClicked.disconnect(self.processResults)
        self.displayLyrics(self.songsData[row])

    def displaySuggestions(self):
        ha = HistoryAnalyzer(self, self.jsondb)
        favArtists = ha.calcFavArtists()
        self.songsData = ha.getSongSuggestions(favArtists)
        self.ui.resultListWidget.itemClicked.connect(self.processResults)
        self.displayResults()
        
    def displayLyrics(self, songData):
        print('AAAAAAAAAAAAAAAAAAAAAAA')
        self.ui.resultListWidget.addItem(songData['Title'])
        self.ui.resultListWidget.addItem(songData['Artist'])
        self.ui.resultListWidget.addItem('Still working')
        songStr = ""
        for part in songData['Lyrics']:
            songStr = songStr + part
        self.ui.resultListWidget.addItem(songStr)

    def searchByLyric(self):

        #self.ui.resultListWidget.itemClicked.connect(self.processResults)
        uInput = str(self.ui.txtUInput.toPlainText())
        results = self.controller.processInput('lyric', uInput, self.jsondb)
        self.songsData = self.controller.getSongsData(results, self.jsondb)
        self.ui.resultListWidget.itemClicked.connect(self.processResults)
        self.displayResults()

    def searchByArtist(self):
        
        #self.ui.resultListWidget.itemClicked.connect(self.processResults)
        uInput = str(self.ui.txtUInput.toPlainText())
        results = self.controller.processInput('artist', uInput, self.jsondb)
        self.songsData = self.controller.getSongsData(results, self.jsondb)
        self.ui.resultListWidget.itemClicked.connect(self.processResults)
        self.displayResults()

    def searchByAlbum(self):
        
        #self.ui.resultListWidget.itemClicked.connect(self.processResults)
        uInput = str(self.ui.txtUInput.toPlainText())
        results = self.controller.processInput('album', uInput, self.jsondb)
        self.songsData = self.controller.getSongsData(results, self.jsondb)
        self.ui.resultListWidget.itemClicked.connect(self.processResults)
        self.displayResults()

    def displayResults(self):
        self.clearResults()
        for data in self.songsData:
            self.ui.resultListWidget.addItem(data['Title'] + " - " + data['Artist'])

    def saveToSearchHistory(self, title, artist):
        #print('Bye')
        sqlt = SQLiteConnector(self)
        stmt = '''select * from searchhistory where songtitle = ? and artist = ?'''
        data = sqlt.readDB(stmt, [title, artist])
        print('data',data)
        if(data == False or data == []):
            print("hey")
            stmt2 = '''insert into searchhistory(songtitle, artist, frequency) values (?, ?, ?)'''
            sqlt.executeOne(stmt2, [title, artist, 1])
        else:
            print("O yay")
            #print(data)
            frequency = int(data[0][2]) + 1
            stmt2 = '''update searchhistory set frequency = ? where songtitle = ? and artist = ?'''
            sqlt.executeOne(stmt2, [frequency, title, artist])
        #print('Hi')

    def clearResults(self):
        self.ui.resultListWidget.clear()