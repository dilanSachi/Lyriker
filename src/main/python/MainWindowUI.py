# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Lyriker(object):
    def setupUi(self, Lyriker):
        Lyriker.setObjectName("Lyriker")
        Lyriker.resize(800, 624)
        self.centralwidget = QtWidgets.QWidget(Lyriker)
        self.centralwidget.setObjectName("centralwidget")
        self.txtUInput = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.txtUInput.setGeometry(QtCore.QRect(200, 50, 401, 31))
        self.txtUInput.setObjectName("txtUInput")
        self.btnLyricSearch = QtWidgets.QPushButton(self.centralwidget)
        self.btnLyricSearch.setGeometry(QtCore.QRect(340, 90, 121, 28))
        self.btnLyricSearch.setObjectName("btnLyricSearch")
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(350, 130, 101, 31))
        self.textEdit_2.setObjectName("textEdit_2")
        self.resultListWidget = QtWidgets.QListWidget(self.centralwidget)
        self.resultListWidget.setGeometry(QtCore.QRect(20, 170, 761, 401))
        self.resultListWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.resultListWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.resultListWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.resultListWidget.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.resultListWidget.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerItem)
        self.resultListWidget.setObjectName("resultListWidget")
        self.btnArtistSearch = QtWidgets.QPushButton(self.centralwidget)
        self.btnArtistSearch.setGeometry(QtCore.QRect(200, 90, 111, 28))
        self.btnArtistSearch.setObjectName("btnArtistSearch")
        self.btnAlbumSearch = QtWidgets.QPushButton(self.centralwidget)
        self.btnAlbumSearch.setGeometry(QtCore.QRect(490, 90, 111, 28))
        self.btnAlbumSearch.setObjectName("btnAlbumSearch")
        self.btnBrowseSongs = QtWidgets.QPushButton(self.centralwidget)
        self.btnBrowseSongs.setGeometry(QtCore.QRect(20, 10, 131, 28))
        self.btnBrowseSongs.setObjectName("btnBrowseSongs")
        self.btnViewSuggestions = QtWidgets.QPushButton(self.centralwidget)
        self.btnViewSuggestions.setGeometry(QtCore.QRect(170, 10, 131, 28))
        self.btnViewSuggestions.setObjectName("btnViewSuggestions")
        Lyriker.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Lyriker)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuView = QtWidgets.QMenu(self.menubar)
        self.menuView.setObjectName("menuView")
        self.menuWindow = QtWidgets.QMenu(self.menubar)
        self.menuWindow.setObjectName("menuWindow")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        Lyriker.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Lyriker)
        self.statusbar.setObjectName("statusbar")
        Lyriker.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuWindow.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(Lyriker)
        QtCore.QMetaObject.connectSlotsByName(Lyriker)

    def retranslateUi(self, Lyriker):
        _translate = QtCore.QCoreApplication.translate
        Lyriker.setWindowTitle(_translate("Lyriker", "MainWindow"))
        self.txtUInput.setToolTip(_translate("Lyriker", "<html><head/><body><p>Search Here</p></body></html>"))
        self.btnLyricSearch.setText(_translate("Lyriker", "Search By Lyric"))
        self.textEdit_2.setHtml(_translate("Lyriker", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">Results</span></p></body></html>"))
        self.btnArtistSearch.setText(_translate("Lyriker", "Search By Artist"))
        self.btnAlbumSearch.setText(_translate("Lyriker", "Search By Album"))
        self.btnBrowseSongs.setText(_translate("Lyriker", "Browse Songs"))
        self.btnViewSuggestions.setText(_translate("Lyriker", "View Suggestions"))
        self.menuFile.setTitle(_translate("Lyriker", "File"))
        self.menuEdit.setTitle(_translate("Lyriker", "Edit"))
        self.menuView.setTitle(_translate("Lyriker", "View"))
        self.menuWindow.setTitle(_translate("Lyriker", "Window"))
        self.menuHelp.setTitle(_translate("Lyriker", "Help"))

