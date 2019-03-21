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
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(220, 20, 331, 31))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(580, 20, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(350, 70, 101, 31))
        self.textEdit_2.setObjectName("textEdit_2")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(20, 120, 761, 421))
        self.listWidget.setObjectName("listWidget")
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
        self.plainTextEdit.setToolTip(_translate("Lyriker", "<html><head/><body><p>Search Here</p></body></html>"))
        self.pushButton.setText(_translate("Lyriker", "Search"))
        self.textEdit_2.setHtml(_translate("Lyriker", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">Results</span></p></body></html>"))
        self.menuFile.setTitle(_translate("Lyriker", "File"))
        self.menuEdit.setTitle(_translate("Lyriker", "Edit"))
        self.menuView.setTitle(_translate("Lyriker", "View"))
        self.menuWindow.setTitle(_translate("Lyriker", "Window"))
        self.menuHelp.setTitle(_translate("Lyriker", "Help"))


