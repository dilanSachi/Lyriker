from fbs_runtime.application_context import ApplicationContext
from PyQt5.QtWidgets import QMainWindow, QMessageBox
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from LetterDeleter import LetterDeleter
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtCore import pyqtSlot
import sys
from test import Ui_Lyriker
from SQLiteConnector import SQLiteConnector
import sqlite3
from JsonOriginalWordCreator import JsonOriginalWordCreator
from JSONManager import JSONManager
from LetterDeleteFormatter import LetterDeleteFormatter
from JsonDB import JsonDB
from Controller import Controller

class AppContext(ApplicationContext):           # 1. Subclass ApplicationContext

    #def __init__(self):
    #    app = QtWidgets.QApplication([])
    #    self.dlg = uic.loadUi("test.ui")
#
#        self.catchSearchBtnClk()
#
#        self.dlg.show()
#        return self.app.exec()

    def __init__(self):
        """database = self.get_resource('lyriker')
        self.db = sqlite3.connect(database)
        #print("afasf")
        self.cursor = self.db.cursor()"""

        self.songsData = []
        self.controller = Controller(self)

        app = QtWidgets.QApplication(sys.argv)
        self.Lyriker = QtWidgets.QMainWindow()
        self.ui = Ui_Lyriker()
        self.ui.setupUi(self.Lyriker)

        self.jsondb = JsonDB(self)
        self.jsondb.loadDeletedWordsDB()
        self.jsondb.loadOriginalWordsDB()
        self.jsondb.loadSongsDB()
        self.jsondb.loadOriginalNamesDB()
        self.jsondb.loadDeletedNamesDB()

        self.catchSearchBtnClk()

        self.Lyriker.show()
        self.app.exec_()

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

if __name__ == '__main__':

    
    appctxt = AppContext()  # 4. Instantiate the subclass

    #lf = JsonOriginalWordCreator(appctxt)
    #lf.formatLyrics()
    #lf.formatArtistNames()

    #print("Done")

    #jm  = JSONManager(appctxt)
    #jm.writeJSON()

    #ldfLyrics = LetterDeleteFormatter(appctxt)
    #ldfLyrics.formatTextAndSaveToJson('OriginalWords.json', 'DeletedWords.json')
    
    #ldfArtistNames = LetterDeleteFormatter(appctxt)
    #ldfArtistNames.formatTextAndSaveToJson('OriginalArtistNames.json', 'DeletedArtistNames.json')
    
    #spn.checkMatchingWords("beautiful")


    #exit_code = appctxt.run()  # 5. Invoke run()
    #sys.exit(exit_code)

