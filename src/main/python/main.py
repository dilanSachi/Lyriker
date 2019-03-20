from fbs_runtime.application_context import ApplicationContext
from PyQt5.QtWidgets import QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from LetterDeleter import LetterDeleter
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtCore import pyqtSlot
import sys
from test import Ui_Lyriker
from SpellCorrector import SpellCorrector
from SQLiteConnector import SQLiteConnector
import sqlite3
from LyricsFormatter import LyricsFormatter
from JSONManager import JSONManager
from LetterDeleteFormatter import LetterDeleteFormatter

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

        self.catchSearchBtnClk()

        self.Lyriker.show()
        self.app.exec_()

    def catchSearchBtnClk(self):
        self.ui.pushButton.clicked.connect(self.getResults)

    def getResults(self):
        uInput = str(self.ui.plainTextEdit.toPlainText()).lower().strip().split(" ")
        ld = LetterDeleter()

        probableWords = []

        for uInputWord in uInput:
            ld.edits = []
            deletedWords = ld.delete(uInputWord, 2)
            deletedWords.append(uInputWord)
            print(deletedWords)

            w = SpellCorrector(self)
#############################################################good for now
            originalWords = []
            originalWordsFrequency =[]

            for deletedWord in deletedWords:
                #print(deletedWord)
                sqltResults = w.search(deletedWord)
                #print(sqltResults)
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
        sqlt = SQLiteConnector(self)
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

        j = 0
        for probableSong in probableSongs:
            if(j==5):
                break
            j = j + 1
            songData = w.getSongData(probableSong-1)
            self.ui.listWidget.addItem("Song : " + songData['Title'])

if __name__ == '__main__':
    print("d")
    appctxt = AppContext()  # 4. Instantiate the subclass

    print("a")

    lf = LyricsFormatter(appctxt)
    lf.formatLyrics()

    print("b")

    #jm  = JSONManager(appctxt)
    #jm.writeJSON()

    ldf = LetterDeleteFormatter(appctxt)
    ldf.format()

    print("c")

    #exit_code = appctxt.run()  # 5. Invoke run()
    #sys.exit(exit_code)

