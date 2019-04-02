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
from Controller import Controller

class MainWindow(ApplicationContext):


    def __init__(self, lyrikerWindow, check):
        super().__init__()

        self.lyrikerWindow = lyrikerWindow

        self.songsData = []
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

    def catchSearchBtnClk(self):
        self.ui.btnLyricSearch.clicked.connect(self.searchByLyric)
        self.ui.btnArtistSearch.clicked.connect(self.searchByArtist)
        
    def processResults(self, item):
        print('jingi biriz')
        row = self.ui.resultListWidget.row(item)
        self.saveToSearchHistory(self.songsData[row]['Title'], self.songsData[row]['Artist'])
        self.clearResults()

        self.displayOther(self.songsData[row])
        
    def displayOther(self, songData):
        self.clearResults()
        self.ui.resultListWidget.itemClicked.disconnect(self.processResults)
        print('hujjariz')
        self.ui.resultListWidget.addItem(songData['Title'])
        self.ui.resultListWidget.addItem(songData['Artist'])
        self.ui.resultListWidget.addItem('Still working')
        songStr = ""
        for part in songData['Lyrics']:
            songStr = songStr + part
        self.ui.resultListWidget.addItem(songStr)

    def searchByLyric(self):
        self.clearResults()
        self.ui.resultListWidget.itemClicked.connect(self.processResults)
        uInput = str(self.ui.txtUInput.toPlainText())
        results = self.controller.processInput('lyric', uInput, self.jsondb)
        self.songsData = self.controller.getSongsData(results, self.jsondb)
        self.displayResults()

    def searchByArtist(self):
        self.clearResults()
        self.ui.resultListWidget.itemClicked.connect(self.processResults)
        uInput = str(self.ui.txtUInput.toPlainText())
        results = self.controller.processInput('artist', uInput, self.jsondb)
        self.songsData = self.controller.getSongsData(results, self.jsondb)
        self.displayResults()

    def displayResults(self):
        for data in self.songsData:
            self.ui.resultListWidget.addItem(data['Title'] + " - " + data['Artist'])

    def saveToSearchHistory(self, title, artist):
        #print('Bye')
        sqlt = SQLiteConnector(self)
        stmt = '''select * from searchhistory where songtitle = ? and artist = ?'''
        data = sqlt.readDB(stmt, [title, artist])
        #print('data',data)
        if(data == False or data == []):
            stmt2 = '''insert into searchhistory(songtitle, artist, frequency) values (?, ?, ?)'''
            sqlt.executeOne(stmt2, [title, artist, 1])
        else:
            #print(data)
            frequency = int(data[0][2]) + 1
            stmt2 = '''update searchhistory set frequency = ? where songtitle = ? and artist = ?'''
            sqlt.executeOne(stmt2, [frequency, title, artist])
        #print('Hi')

    def clearResults(self):
        self.ui.resultListWidget.clear()