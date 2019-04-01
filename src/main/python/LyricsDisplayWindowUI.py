# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'lyricsdisplaywindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Lyrics(object):
    def setupUi(self, Lyrics):
        Lyrics.setObjectName("Lyrics")
        Lyrics.resize(800, 606)
        self.centralwidget = QtWidgets.QWidget(Lyrics)
        self.centralwidget.setObjectName("centralwidget")
        self.lblTitle = QtWidgets.QLabel(self.centralwidget)
        self.lblTitle.setGeometry(QtCore.QRect(210, 20, 371, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lblTitle.setFont(font)
        self.lblTitle.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lblTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.lblTitle.setObjectName("lblTitle")
        self.lblArtist = QtWidgets.QLabel(self.centralwidget)
        self.lblArtist.setGeometry(QtCore.QRect(20, 60, 371, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lblArtist.setFont(font)
        self.lblArtist.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lblArtist.setAlignment(QtCore.Qt.AlignCenter)
        self.lblArtist.setObjectName("lblArtist")
        self.lblAlbum = QtWidgets.QLabel(self.centralwidget)
        self.lblAlbum.setGeometry(QtCore.QRect(420, 60, 371, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lblAlbum.setFont(font)
        self.lblAlbum.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lblAlbum.setAlignment(QtCore.Qt.AlignCenter)
        self.lblAlbum.setObjectName("lblAlbum")
        self.listLyrics = QtWidgets.QListWidget(self.centralwidget)
        self.listLyrics.setGeometry(QtCore.QRect(15, 111, 771, 441))
        self.listLyrics.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.listLyrics.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.listLyrics.setObjectName("listLyrics")
        self.btnBack = QtWidgets.QPushButton(self.centralwidget)
        self.btnBack.setGeometry(QtCore.QRect(10, 10, 93, 28))
        self.btnBack.setObjectName("btnBack")
        Lyrics.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Lyrics)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        Lyrics.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Lyrics)
        self.statusbar.setObjectName("statusbar")
        Lyrics.setStatusBar(self.statusbar)

        self.retranslateUi(Lyrics)
        QtCore.QMetaObject.connectSlotsByName(Lyrics)

    def retranslateUi(self, Lyrics):
        _translate = QtCore.QCoreApplication.translate
        Lyrics.setWindowTitle(_translate("Lyrics", "Lyrics"))
        self.lblTitle.setText(_translate("Lyrics", "TextLabel"))
        self.lblArtist.setText(_translate("Lyrics", "TextLabel"))
        self.lblAlbum.setText(_translate("Lyrics", "TextLabel"))
        self.btnBack.setText(_translate("Lyrics", "Back"))

