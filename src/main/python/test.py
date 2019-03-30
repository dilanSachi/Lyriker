# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Lyriker(object):
    def setupUi(self, Lyriker):
        Lyriker.setObjectName("Lyriker")
        Lyriker.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(Lyriker)
        self.centralwidget.setObjectName("centralwidget")
        self.txtUInput = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.txtUInput.setGeometry(QtCore.QRect(200, 50, 391, 31))
        self.txtUInput.setObjectName("txtUInput")
        self.btnLyricSearch = QtWidgets.QPushButton(self.centralwidget)
        self.btnLyricSearch.setGeometry(QtCore.QRect(340, 90, 121, 28))
        self.btnLyricSearch.setObjectName("btnLyricSearch")
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(350, 130, 101, 31))
        self.textEdit_2.setObjectName("textEdit_2")
        self.resultListWidget = QtWidgets.QListWidget(self.centralwidget)
        self.resultListWidget.setGeometry(QtCore.QRect(20, 170, 761, 371))
        self.resultListWidget.setObjectName("resultListWidget")
        self.btnArtistSearch = QtWidgets.QPushButton(self.centralwidget)
        self.btnArtistSearch.setGeometry(QtCore.QRect(200, 90, 111, 28))
        self.btnArtistSearch.setObjectName("btnArtistSearch")
        self.btnTitleSearch = QtWidgets.QPushButton(self.centralwidget)
        self.btnTitleSearch.setGeometry(QtCore.QRect(490, 90, 101, 28))
        self.btnTitleSearch.setObjectName("btnTitleSearch")
        self.btnBrowseSongs = QtWidgets.QPushButton(self.centralwidget)
        self.btnBrowseSongs.setGeometry(QtCore.QRect(20, 10, 131, 28))
        self.btnBrowseSongs.setObjectName("btnBrowseSongs")
        self.btnViewSuggestoins = QtWidgets.QPushButton(self.centralwidget)
        self.btnViewSuggestoins.setGeometry(QtCore.QRect(170, 10, 131, 28))
        self.btnViewSuggestoins.setObjectName("btnViewSuggestoins")
        self.verticalScrollBar = QtWidgets.QScrollBar(self.centralwidget)
        self.verticalScrollBar.setGeometry(QtCore.QRect(760, 170, 21, 371))
        self.verticalScrollBar.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar.setObjectName("verticalScrollBar")
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
        self.btnTitleSearch.setText(_translate("Lyriker", "Search By Title"))
        self.btnBrowseSongs.setText(_translate("Lyriker", "Browse Songs"))
        self.btnViewSuggestoins.setText(_translate("Lyriker", "View Suggestions"))
        self.menuFile.setTitle(_translate("Lyriker", "File"))
        self.menuEdit.setTitle(_translate("Lyriker", "Edit"))
        self.menuView.setTitle(_translate("Lyriker", "View"))
        self.menuWindow.setTitle(_translate("Lyriker", "Window"))
        self.menuHelp.setTitle(_translate("Lyriker", "Help"))

