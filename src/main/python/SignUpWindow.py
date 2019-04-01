from fbs_runtime.application_context import ApplicationContext
from PyQt5.QtWidgets import QMainWindow, QMessageBox
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from LetterDeleter import LetterDeleter
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtCore import pyqtSlot
from SignUpUI import Ui_signUpWindow
import sys
from SQLiteConnector import SQLiteConnector
from MainWindow import MainWindow

class SignUpWindow(ApplicationContext):

    def __init__(self, qMainWindow):
        """
        #app = QtWidgets.QApplication(sys.argv)
        print("Sign up init")
        self.Lyriker = QtWidgets.QMainWindow()
        self.ui = Ui_signUpWindow()
        self.ui.setupUi(self.Lyriker)

        self.catchSignUpBtnClk()

        self.Lyriker.show()
        print("asfasfasfaasfasfas")
        #sys.exit(self.app.exec_())"""
        #app = QtWidgets.QApplication(sys.argv)
        self.qMainWindow = qMainWindow
        print("Sign up init")
        self.ui = Ui_signUpWindow()
        self.ui.setupUi(self.qMainWindow)

        self.catchSignUpBtnClk()

        self.qMainWindow.show()
        print("asfasfasfaasfasfas")
        sys.exit(self.app.exec_())

    def catchSignUpBtnClk(self):
        self.ui.btnSignUp.clicked.connect(self.signUp)

    def signUp(self):
        print('btn clck')
        username = str(self.ui.txtUsername.text())
        email = str(self.ui.txtEmail.text())
        stmt = 'insert into users(username, email) values (?, ?)'
        sqlt = SQLiteConnector(self)
        if(sqlt.executeOne(stmt, [username, email])):
            self.qMainWindow.hide()
            MainWindow(self.qMainWindow)
            #self.close()
            #self.Lyriker.close()
            #self.app.exit()
            #QtWidgets.qApp.quit()
            #MainWindow()
        else:
            print('error')
           # QMessageBox.information("Error in database")

