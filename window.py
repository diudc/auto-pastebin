

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QInputDialog, QLineEdit, QFileDialog
import auto_pastebin
import getpass
import pyperclip
class Ui_MainWindow(QtWidgets.QWidget):
    fileName=""
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(410, 502)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.paste = QtWidgets.QPushButton(self.centralwidget)
        self.paste.setGeometry(QtCore.QRect(120, 360, 151, 41))
        self.paste.setObjectName("paste")
        self.paste.clicked.connect(self.paster)
        self.code = QtWidgets.QTextEdit(self.centralwidget)
        self.code.setGeometry(QtCore.QRect(13, 160, 381, 191))
        self.code.setObjectName("code")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 140, 47, 13))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.op = QtWidgets.QPushButton(self.centralwidget)
        self.op.setGeometry(QtCore.QRect(10, 90, 91, 41))
        self.op.setObjectName("op")
        self.op.clicked.connect(self.openfile)
        self.fname = QtWidgets.QLabel(self.centralwidget)
        self.fname.setGeometry(QtCore.QRect(120, 90, 271, 41))
        self.fname.setText("")
        self.fname.setObjectName("fname")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 430, 51, 21))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.urll = QtWidgets.QLabel(self.centralwidget)
        self.urll.setGeometry(QtCore.QRect(60, 430, 321, 21))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.urll.setFont(font)
        self.urll.setText("")
        self.urll.setObjectName("urll")
        self.namel = QtWidgets.QLabel(self.centralwidget)
        self.namel.setGeometry(QtCore.QRect(40, 30, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.namel.setFont(font)
        self.namel.setObjectName("namel")
        self.namef = QtWidgets.QLineEdit(self.centralwidget)
        self.namef.setGeometry(QtCore.QRect(120, 30, 231, 31))
        self.namef.setObjectName("namef")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 410, 21))
        self.menubar.setObjectName("menubar")
        self.menuPasteBinIt = QtWidgets.QMenu(self.menubar)
        self.menuPasteBinIt.setObjectName("menuPasteBinIt")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuPasteBinIt.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.paste.setText(_translate("MainWindow", "Paste"))
        self.label_2.setText(_translate("MainWindow", "Text"))
        self.op.setText(_translate("MainWindow", "Open a file"))
        self.label_3.setText(_translate("MainWindow", "URL:"))
        self.namel.setText(_translate("MainWindow", "Name :"))
        self.namef.setPlaceholderText(_translate("MainWindow", "Leave empty for your username"))
        self.menuPasteBinIt.setTitle(_translate("MainWindow", "PasteBinIt"))
    
    def openfile(self):
        _translate = QtCore.QCoreApplication.translate
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        self.fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","All Files (*);;Python Files (*.py)", options=options)
        if self.fileName!="":
            #print(self.fileName)
            self.fname.setText(_translate("MainWindow", self.fileName))
            data=auto_pastebin.read_file(self.fileName)
            self.code.setText(data)

    def paster(self):
        data=""
        if self.namef.text()=="":
            data= {
	            'poster':getpass.getuser(),
	            'syntax':'text',
	            'content': self.code.toPlainText()
	        }
        else:
             data= {
	            'poster':self.namef.text(),
	            'syntax':'text',
	            'content': self.code.toPlainText()
	        }
        #print(data)
        response=auto_pastebin.post_req(data,"https://pastebin.ubuntu.com/")
        if response.ok:
           #print(response.url,response.status_code)
           self.urll.setText(response.url)
           pyperclip.copy(response.url)
        else:
           self.urll.setText("Error!")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
