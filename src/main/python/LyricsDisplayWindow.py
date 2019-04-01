from fbs_runtime.application_context import ApplicationContext
from PyQt5.QtWidgets import QMainWindow, QMessageBox
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtCore import pyqtSlot
import sys
from LyricsDisplayWindowUI import Ui_Lyrics
from SQLiteConnector import SQLiteConnector
import sqlite3
from Controller import Controller
from MainWindowUI import Ui_Lyriker

class LyricsDisplayWindow(ApplicationContext):

    def __init__(self, lyrikerWindow, songData, mainWindow):
        super().__init__()

        self.lyrikerWindow = QtWidgets.QMainWindow()

        self.mainWindow = mainWindow
        self.lyriker = lyrikerWindow
        self.ui = Ui_Lyrics()
        self.ui.setupUi(self.lyrikerWindow)
        self.setSongDataToUI(songData)
        
        self.lyrikerWindow.show()
        self.catchButtonClick()

        #self.qMainWindow.show()
        #sys.exit(self.app.exec_())

    def catchButtonClick(self):
        print('connected')
        self.ui.btnBack.clicked.connect(self.goBackToMainWindow)

    def goBackToMainWindow(self):
        print('hgc')
        self.lyrikerWindow.hide()
        #self.ui = Ui_Lyriker()
        #self.ui.setupUi(self.lyrikerWindow)
        #self.mainWindow.loadJsonFiles()
        self.lyriker.show()
        #self.mainWindow.catchSearchBtnClk()
        self.mainWindow.displayResults()
        

    def setSongDataToUI(self, songData):
        self.ui.lblTitle.setText(songData['Title'])
        self.ui.lblArtist.setText(songData['Artist'])
        self.ui.lblAlbum.setText('Still working')
        songStr = ""
        for part in songData['Lyrics']:
            songStr = songStr + part
        self.ui.listLyrics.addItem(songStr)

    
