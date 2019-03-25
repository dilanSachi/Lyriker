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
from LyricsFormatter import LyricsFormatter
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

        self.catchSearchBtnClk()

        self.Lyriker.show()
        self.app.exec_()

    def catchSearchBtnClk(self):
        self.ui.pushButton.clicked.connect(self.test)
        #self.ui.pushButton.clicked.connect(self.getResults)

    def test(self):
        controller = Controller(self)
        uInput = str(self.ui.plainTextEdit.toPlainText())
        results = controller.processUInput(uInput, self.jsondb)
        songData = controller.processSongResults(results, self.jsondb)
        for data in songData:
            self.ui.listWidget.addItem(data['Title'])

    
            #self.ui.listWidget.addItem("Song : " + songData['Title'])

if __name__ == '__main__':

    
    appctxt = AppContext()  # 4. Instantiate the subclass

    #lf = LyricsFormatter(appctxt)
    #lf.formatLyrics()

    #print("Done")

    #jm  = JSONManager(appctxt)
    #jm.writeJSON()

    #ldf = LetterDeleteFormatter(appctxt)
    #ldf.format()

    
    #spn.checkMatchingWords("beautiful")


    #exit_code = appctxt.run()  # 5. Invoke run()
    #sys.exit(exit_code)

