from fbs_runtime.application_context import ApplicationContext
from PyQt5.QtWidgets import QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from MySqlConnector import MySqlConnector
from LetterDeleter import LetterDeleter
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtCore import pyqtSlot
import sys
from Words import Words

class AppContext(ApplicationContext):           # 1. Subclass ApplicationContext

    def __init__(self):
        app = QtWidgets.QApplication([])
        self.dlg = uic.loadUi("test.ui")

        self.catchSearchBtnClk()

        self.dlg.show()
        self.app.exec()

    def catchSearchBtnClk(self):
        self.dlg.pushButton.clicked.connect(self.getResults)

    def getResults(self):
        uInput = str(self.dlg.plainTextEdit.toPlainText()).lower().strip().split(" ")
        ld = LetterDeleter()

        songs = []
        frequency = []

        for uInputWord in uInput:
            ld.edits = []
            deletedWords = ld.delete(uInputWord, 2)
            deletedWords.append(uInputWord)

            w = Words()
            tempSongs = []                              #wadipurama galapena wachane aran eka tina sinduwa hyano
            tempFrequency = []
            for deletedWord in deletedWords:
                #print(deletedWord)
                sqltResults = w.search(deletedWord)

                for sqltResult in sqltResults:
                    try:
                        ind = tempSongs.index(sqltResult)
                        tempFrequency[ind] = tempFrequency[ind] + 1
                    except:
                        tempSongs.append(sqltResult)
                        tempFrequency.append(1)

            for tempSong in tempSongs:
                #self.dlg.listWidget.addItem("Original Word : " + str(originalWord[0]))
                maxInd = tempFrequency.index(max(tempFrequency))
                #print(songs[maxInd])
                try:
                    ind = songs.index(tempSongs[maxInd])
                    frequency[ind] = frequency[ind] + 1
                except:
                    songs.append(tempSongs[maxInd])
                    frequency.append(1)
                tempFrequency[maxInd] = 0
        #print(tempSongs)
        #print(tempFrequency)
        w = Words()
        songsData = w.getSongData()
        print(songs)
        print(frequency)
        for song in songs:
            #self.dlg.listWidget.addItem("Original Word : " + str(originalWord[0]))
            maxInd = frequency.index(max(frequency))
            #print(songs[maxInd])

            print(songsData[songs[maxInd]-1])
            frequency[maxInd] = 0
                #self.dlg.listWidget.addItem("Original Word : "+str(originalWord[0]))
                    #self.dlg.listWidget.addItem("Song : "+ str(song[0]))
        #self.dlg.listWidget.hide()
        #self.dlg.listWidget.show()

        #print(self.dlg.plainTextEdit.toPlainText())

ap = AppContext()
