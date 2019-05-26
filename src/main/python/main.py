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
from JsonOriginalWordCreator import JsonOriginalWordCreator
from LetterDeleteFormatter import LetterDeleteFormatter

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
        self.lyrikerWindow = QtWidgets.QMainWindow()
        #self.ui = Ui_Dialog()
        #self.ui.setupUi(self.Lyriker)
        self.loadUi()
        sys.exit(app.exec_())

    def loadUi(self):
        sqlt = SQLiteConnector(self)
        if(sqlt.checkDB()):
            MainWindow(self.lyrikerWindow, False)
        else:
            SignUpWindow(self.lyrikerWindow)
            
class Test(ApplicationContext):

    def printer(self):
        print("Test")


if __name__ == '__main__':

    
    main = Main()  # 4. Instantiate the subclass    
"""
    main = Test()

    print("asf")

    lf = JsonOriginalWordCreator(main)
    lf.formatLyrics()
    lf.formatArtistNames()
    lf.formatAlbumNames()

    print("Done")

    ldfLyrics = LetterDeleteFormatter(main)
    ldfLyrics.formatTextAndSaveToJson('OriginalWords.json', 'DeletedWords.json')
    
    ldfArtistNames = LetterDeleteFormatter(main)
    ldfArtistNames.formatTextAndSaveToJson('OriginalArtistNames.json', 'DeletedArtistNames.json')

    ldfAlbumNames = LetterDeleteFormatter(main)
    ldfAlbumNames.formatTextAndSaveToJson('OriginalAlbumNames.json', 'DeletedAlbumNames.json')
 
"""

    #exit_code = appctxt.run()  # 5. Invoke run()
    #sys.exit(exit_code)
