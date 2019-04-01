from fbs_runtime.application_context import ApplicationContext
from PyQt5.QtWidgets import QMainWindow, QMessageBox
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from LetterDeleter import LetterDeleter
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtCore import pyqtSlot
import sys
from MainWindowUI import Ui_Lyriker
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
        self.ui.resultListWidget.itemClicked.connect(self.Clicked)
        
    def Clicked(self, item):
        row = self.ui.resultListWidget.row(item)
        self.clearResults()
        self.controller.displaySongLyric(self.ui.resultListWidget, self.songsData[row])
        #QMessageBox.information(self.ui.resultListWidget, "ListWidget", "You clicked: "+item.text())

    def searchByLyric(self):
        uInput = str(self.ui.txtUInput.toPlainText())
        results = self.controller.processInput('lyric', uInput, self.jsondb)
        self.songsData = self.controller.getSongsData(results, self.jsondb)
        for data in self.songsData:
            self.ui.resultListWidget.addItem(data['Title'] + " - " + data['Artist'])

    def searchByArtist(self):
        uInput = str(self.ui.txtUInput.toPlainText())
        results = self.controller.processInput('artist', uInput, self.jsondb)
        self.songsData = self.controller.getSongsData(results, self.jsondb)
        for data in self.songsData:
            self.ui.resultListWidget.addItem(data['Title'] + " - " + data['Artist'])

    def clearResults(self):
        self.ui.resultListWidget.clear()