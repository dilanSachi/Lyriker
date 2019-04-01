from fbs_runtime.application_context import ApplicationContext
from PyQt5.QtWidgets import QMainWindow, QMessageBox
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from LetterDeleter import LetterDeleter
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtCore import pyqtSlot
import sys
from MainWindowUI import Ui_Lyriker
from LyricsDisplayWindow import LyricsDisplayWindow
from SQLiteConnector import SQLiteConnector
import sqlite3
from JsonDB import JsonDB
from Controller import Controller

class MainWindow(ApplicationContext):

    def __init__(self, qMainWindow):

        self.songsData = []
        self.controller = Controller(self)

        #app = QtWidgets.QApplication(sys.argv)
        #self.Lyriker = QtWidgets.QMainWindow()
        self.qMainWindow = qMainWindow
        self.ui = Ui_Lyriker()
        self.ui.setupUi(self.qMainWindow)

        self.loadJsonFiles()
        self.catchSearchBtnClk()

        self.qMainWindow.show()
        ##self.app.exec_()
        #sys.exit(self.app.exec_())

    def loadJsonFiles(self):
        self.jsondb = JsonDB(self)
        self.jsondb.loadDeletedWordsDB()
        self.jsondb.loadOriginalWordsDB()
        self.jsondb.loadSongsDB()
        self.jsondb.loadOriginalNamesDB()
        self.jsondb.loadDeletedNamesDB()

    def catchSearchBtnClk(self):
        self.clearResults()
        self.ui.btnLyricSearch.clicked.connect(self.searchByLyric)
        self.ui.btnArtistSearch.clicked.connect(self.searchByArtist)
        self.ui.resultListWidget.itemClicked.connect(self.processResults)
        
    def processResults(self, item):
        row = self.ui.resultListWidget.row(item)
        self.saveToSearchHistory(self.songsData[row]['Title'], self.songsData[row]['Artist'])
        self.clearResults()
        self.qMainWindow.hide()
        LyricsDisplayWindow(self.qMainWindow, self.songsData[row])
        #self.displaySongLyric(self.ui.resultListWidget, self.songsData[row])
        
        #QMessageBox.information(self.ui.resultListWidget, "ListWidget", "You clicked: "+item.text())

    def searchByLyric(self):
        uInput = str(self.ui.txtUInput.toPlainText())
        results = self.controller.processInput('lyric', uInput, self.jsondb)
        self.songsData = self.controller.getSongsData(results, self.jsondb)
        self.displayResults(self.songsData)

    def searchByArtist(self):
        uInput = str(self.ui.txtUInput.toPlainText())
        results = self.controller.processInput('artist', uInput, self.jsondb)
        self.songsData = self.controller.getSongsData(results, self.jsondb)
        self.displayResults(self.songsData)

    def displayResults(self, songsData):
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