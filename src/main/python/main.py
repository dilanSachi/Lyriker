from fbs_runtime.application_context import ApplicationContext
from PyQt5.QtWidgets import QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from LetterDeleter import LetterDeleter
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtCore import pyqtSlot
import sys
from Words import Words
from SQLiteConnector import SQLite

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

        probableWords = []

        for uInputWord in uInput:
            ld.edits = []
            deletedWords = ld.delete(uInputWord, 2)
            deletedWords.append(uInputWord)

            w = Words()

            originalWords = []
            originalWordsFrequency =[]

            for deletedWord in deletedWords:
                #print(deletedWord)
                sqltResults = w.search(deletedWord)
                sqltOriginalWords = sqltResults[0]
                sqltSongs = sqltResults[1]

                tempOriginalWords = []  # wadipurama galapena wachane aran eka tina sinduwa hyano

                for sqltOriginalWord in sqltOriginalWords:
                    try:
                        ind = tempOriginalWords.index(sqltOriginalWord)
                    except:
                        tempOriginalWords.append(sqltOriginalWord)

                for tempOriginalWord in tempOriginalWords:

                    try:
                        ind = originalWords.index(tempOriginalWord)
                        originalWordsFrequency[ind] = originalWordsFrequency[ind] + 1
                    except:
                        originalWords.append(tempOriginalWord)
                        originalWordsFrequency.append(1)


            #print("ow",originalWords)
            #print("owfo",originalWordsFrequency)

            temp = []
            for i in range(len(originalWords)):
                ind = originalWordsFrequency.index(max(originalWordsFrequency))
                temp.append(originalWords[ind])
                originalWordsFrequency[ind] = 0
                if(i==0):
                    break
            probableWords.append(temp)
        #print("final",probableWords)
        sqlt = SQLite()
        probableSongs = []
        probableSongsFrequency = []
        tempI = []
        print(probableWords)
        i = 0
        for temp in probableWords:
            for ind in temp:
                results = sqlt.test(ind)
                #print(result)
                for result in results:
                    try:
                        tempInd = probableSongs.index(result[1])
                        if(i != tempI[tempInd]):
                            probableSongsFrequency[tempInd] = probableSongsFrequency[tempInd] + 1
                    except:
                        probableSongs.append(result[1])
                        probableSongsFrequency.append(1)
                        tempI.append(i)
            i = i + 1
        print(probableSongs)
        print(probableSongsFrequency)

        for probableSong in probableSongs:
            #print(probableSong)
            songData = w.getSongData(probableSong-1)
            self.dlg.listWidget.addItem("Song : " + songData['Title'])
        #print(tempSongs)
        #print(tempFrequency)
        #w = Words()
       # songsData = w.getSongData()
        #print(songs)
        #print(frequency)
        #for song in songs:
            #self.dlg.listWidget.addItem("Original Word : " + str(originalWord[0]))
           # maxInd = frequency.index(max(frequency))
            #print(songs[maxInd])

           # print(songsData[songs[maxInd]-1])
           # frequency[maxInd] = 0
                #self.dlg.listWidget.addItem("Original Word : "+str(originalWord[0]))
                    #self.dlg.listWidget.addItem("Song : "+ str(song[0]))
        #self.dlg.listWidget.hide()
        #self.dlg.listWidget.show()

        #print(self.dlg.plainTextEdit.toPlainText())

ap = AppContext()
