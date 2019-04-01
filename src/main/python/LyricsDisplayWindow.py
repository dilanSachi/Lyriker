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

class LyricsDisplayWindow(ApplicationContext):

    def __init__(self, qMainWindow, songData):

        self.qMainWindow = qMainWindow
        self.ui = Ui_Lyrics()
        self.ui.setupUi(self.qMainWindow)
        self.setSongDataToUI(songData)
        self.qMainWindow.show()

    def setSongDataToUI(self, songData):
        self.ui.lblTitle.setText(songData['Title'])
        self.ui.lblArtist.setText(songData['Artist'])
        self.ui.lblAlbum.setText('Still working')
        songStr = ""
        for part in songData['Lyrics']:
            songStr = songStr + part
        self.ui.listLyrics.addItem(songStr)

    