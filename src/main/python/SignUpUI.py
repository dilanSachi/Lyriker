# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'signup.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_signUpWindow(object):
    def setupUi(self, signUpWindow):
        signUpWindow.setObjectName("signUpWindow")
        signUpWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(signUpWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(280, 80, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.txtUsername = QtWidgets.QLineEdit(self.centralwidget)
        self.txtUsername.setGeometry(QtCore.QRect(360, 181, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.txtUsername.setFont(font)
        self.txtUsername.setObjectName("txtUsername")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(200, 190, 141, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(200, 249, 141, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.txtEmail = QtWidgets.QLineEdit(self.centralwidget)
        self.txtEmail.setGeometry(QtCore.QRect(360, 240, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.txtEmail.setFont(font)
        self.txtEmail.setObjectName("txtEmail")
        self.btnSignUp = QtWidgets.QPushButton(self.centralwidget)
        self.btnSignUp.setGeometry(QtCore.QRect(510, 300, 93, 28))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btnSignUp.setFont(font)
        self.btnSignUp.setObjectName("btnSignUp")
        signUpWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(signUpWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        signUpWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(signUpWindow)
        self.statusbar.setObjectName("statusbar")
        signUpWindow.setStatusBar(self.statusbar)

        self.retranslateUi(signUpWindow)
        QtCore.QMetaObject.connectSlotsByName(signUpWindow)

    def retranslateUi(self, signUpWindow):
        _translate = QtCore.QCoreApplication.translate
        signUpWindow.setWindowTitle(_translate("signUpWindow", "Lyriker Sign Up"))
        self.label.setText(_translate("signUpWindow", "Welcome To Lyriker"))
        self.label_2.setText(_translate("signUpWindow", "Enter Username :"))
        self.label_3.setText(_translate("signUpWindow", "Enter Email :"))
        self.btnSignUp.setText(_translate("signUpWindow", "Sign Up"))

