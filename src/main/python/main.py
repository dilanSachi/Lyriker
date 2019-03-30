from fbs_runtime.application_context import ApplicationContext
from PyQt5.QtWidgets import QMainWindow
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
        self.ui.btnLyricSearch.clicked.connect(self.searchByLyric)
        #self.ui.btnTitleSearch.clicked.connect(self.test)
        self.ui.btnArtistSearch.clicked.connect(self.searchByArtist)

    def searchByLyric(self):
        controller = Controller(self)
        uInput = str(self.ui.plainTextEdit.toPlainText())
        results = controller.processLyricInput(uInput, self.jsondb)
        songData = controller.getSongData(results, self.jsondb)
        for data in songData:
            self.ui.listWidget.addItem(data['Title'])

    def searchByArtist(self):
        controller = Controller(self)
        uInput = str(self.ui.plainTextEdit.toPlainText())
        results = controller.processArtistNameInput(uInput, self.jsondb)
        print(results)
        songData = controller.getSongData(results, self.jsondb)
        for data in songData:
            self.ui.listWidget.addItem(data['Title'] + " - " + data['Artist'])

    #def searchByTitle(self):
    
            #self.ui.listWidget.addItem("Song : " + songData['Title'])

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

