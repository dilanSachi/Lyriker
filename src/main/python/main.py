from fbs_runtime.application_context import ApplicationContext
from PyQt5.QtWidgets import QMainWindow, QMessageBox
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from LetterDeleter import LetterDeleter
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtCore import pyqtSlot
import sys
from MainWindow import MainWindow
from SignUpWindow import SignUpWindow
from SQLiteConnector import SQLiteConnector
import sqlite3
from JsonDB import JsonDB
from Controller import Controller

class Main(ApplicationContext):           # 1. Subclass ApplicationContext

    #def __init__(self):
    #    app = QtWidgets.QApplication([])
    #    self.dlg = uic.loadUi("test.ui")
#
#        self.catchSearchBtnClk()
#
#        self.dlg.show()
#        return self.app.exec()

    def __init__(self):
        app = QtWidgets.QApplication(sys.argv)
        self.Lyriker = QtWidgets.QMainWindow()
        self.loadUi()
        sys.exit(self.app.exec_())

    def loadUi(self):
        sqlt = SQLiteConnector(self)
        if(sqlt.checkDB()):
            MainWindow(self.Lyriker)
        else:
            SignUpWindow(self.Lyriker)

if __name__ == '__main__':

    
    main = Main()  # 4. Instantiate the subclass

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