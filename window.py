

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QInputDialog, QLineEdit, QFileDialog
import auto_pastebin
import getpass
import pyperclip
class Ui_MainWindow(QtWidgets.QWidget):
    fileName=""
    def setupUi(self, MainWindow):
        #window
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(410, 502)

        #fonts
        font_calibri_14 = QtGui.QFont()
        font_calibri_14.setFamily("Calibri")
        font_calibri_14.setPointSize(14)
        font_calibri_12 = QtGui.QFont()
        font_calibri_12.setFamily("Calibri")
        font_calibri_12.setPointSize(12)
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.paste_btn= QtWidgets.QPushButton(self.centralwidget)
        self.paste_btn.setGeometry(QtCore.QRect(120, 360, 151, 41))
        self.paste_btn.setObjectName("paste_btn")
        self.paste_btn.clicked.connect(self.paster)

        self.code_box = QtWidgets.QTextEdit(self.centralwidget)
        self.code_box.setGeometry(QtCore.QRect(13, 160, 381, 191))
        self.code_box.setObjectName("code_box")
        
        self.code_box_label = QtWidgets.QLabel(self.centralwidget)
        self.code_box_label.setGeometry(QtCore.QRect(20, 140, 47, 13))
        self.code_box_label.setFont(font_calibri_12)
        self.code_box_label.setObjectName("code_box_label")

        self.open_file_btn = QtWidgets.QPushButton(self.centralwidget)
        self.open_file_btn.setGeometry(QtCore.QRect(10, 90, 91, 41))
        self.open_file_btn.setObjectName("open_file_btn")
        self.open_file_btn.clicked.connect(self.openfile)

        self.file_name_label = QtWidgets.QLabel(self.centralwidget)
        self.file_name_label.setGeometry(QtCore.QRect(120, 90, 271, 41))
        self.file_name_label.setText("")
        self.file_name_label.setObjectName("file_name_label")

        self.url_label = QtWidgets.QLabel(self.centralwidget)
        self.url_label.setGeometry(QtCore.QRect(20, 430, 51, 21))
        self.url_label.setFont(font_calibri_14)
        self.url_label.setObjectName("url_label")


        self.url_text = QtWidgets.QLabel(self.centralwidget)
        self.url_text.setGeometry(QtCore.QRect(60, 430, 321, 21))
        self.url_text.setFont(font_calibri_12)
        self.url_text.setText("")
        self.url_text.setObjectName("url_text")
        
        self.username_lable = QtWidgets.QLabel(self.centralwidget)
        self.username_lable.setGeometry(QtCore.QRect(40, 30, 61, 31))
        self.username_lable.setFont(font_calibri_14)
        self.username_lable.setObjectName("username_lable")


        self.username_input_field = QtWidgets.QLineEdit(self.centralwidget)
        self.username_input_field.setGeometry(QtCore.QRect(120, 30, 231, 31))
        self.username_input_field.setObjectName("username_input_field")
        
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
        self.paste_btn.setText(_translate("MainWindow", "Paste"))
        self.code_box_label.setText(_translate("MainWindow", "Text"))
        self.open_file_btn.setText(_translate("MainWindow", "Open a file"))
        self.url_label.setText(_translate("MainWindow", "URL:"))
        self.username_lable.setText(_translate("MainWindow", "Name :"))
        self.username_input_field.setPlaceholderText(_translate("MainWindow", "Leave empty for your username"))
        self.menuPasteBinIt.setTitle(_translate("MainWindow", "PasteBinIt"))
    
    def openfile(self):
        _translate = QtCore.QCoreApplication.translate
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        self.fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","All Files (*);;Python Files (*.py)", options=options)
        if self.fileName!="":
            self.fname.setText(_translate("MainWindow", self.fileName))
            data=auto_pastebin.read_file(self.fileName)
            self.code_box.setText(data)

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
        response=auto_pastebin.post_req(data,"https://pastebin.ubuntu.com/")
        if response.ok:
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
