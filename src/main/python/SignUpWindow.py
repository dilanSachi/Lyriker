from fbs_runtime.application_context import ApplicationContext
from PyQt5.QtWidgets import QMainWindow, QMessageBox
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from LetterDeleter import LetterDeleter
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtCore import pyqtSlot
import sys
from SignUpUI import Ui_signUpWindow
from SQLiteConnector import SQLiteConnector
from MainWindow import MainWindow

class SignUpWindow(ApplicationContext):

    def __init__(self, lyrikerWindow):
        super().__init__()

        self.lyrikerWindow = lyrikerWindow
        #self.qMainWindow = qMainWindow
        print("Sign up init")
        self.ui = Ui_signUpWindow()
        self.ui.setupUi(self.lyrikerWindow)

        self.lyrikerWindow.show()

        self.catchSignUpBtnClk()
        
        #self.qMainWindow.show()
        #print("asfasfasfaasfasfas")
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
            self.lyrikerWindow.hide()
            # self.qMainWindow.hide()
            MainWindow(self.lyrikerWindow, True)
            #self.close()
            #self.Lyriker.close()
            #self.app.exit()
            #QtWidgets.qApp.quit()
            #MainWindow()
        else:
            print('error')
           # QMessageBox.information("Error in database")

