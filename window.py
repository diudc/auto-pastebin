

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
        MainWindow.resize(500, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        #fonts
        font_calibri_14 = QtGui.QFont()
        font_calibri_14.setFamily("Calibri")
        font_calibri_14.setPointSize(14)
        font_calibri_12 = QtGui.QFont()
        font_calibri_12.setFamily("Calibri")
        font_calibri_12.setPointSize(12)
        font_code=QtGui.QFont()
        font_code.setFamily("Courier")
        font_code.setStyleHint(QtGui.QFont.Monospace)
        font_code.setFixedPitch(True)
        font_code.setPointSize(12)

        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 500, 500))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        # self.verticalLayoutWidget.setSizePolicy(sizePolicy)
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(5, 5, 5,5)
        self.verticalLayout.setObjectName("verticalLayout")

        #h1= first horizontal layout
        self.h1 = QtWidgets.QHBoxLayout()
        self.h1.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.h1.setObjectName("h1")
        self.h1.setContentsMargins(5,5,5,5)
        
        self.username_lable = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.username_lable.setFont(font_calibri_14)
        self.username_lable.setObjectName("username_lable")
        
        self.username_input_field = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.username_input_field.setObjectName("username_input_field")
        
        self.h1.addWidget(self.username_lable)
        self.h1.addWidget(self.username_input_field)

        #h2= second horizontal layout
        self.h2 = QtWidgets.QHBoxLayout()
        self.h2.setObjectName("h2")
        self.h2.setContentsMargins(5,5,5,5)

        self.open_file_btn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.open_file_btn.setObjectName("open_file_btn")
        self.open_file_btn.clicked.connect(self.openfile)
        self.open_file_btn.setSizePolicy(QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum))

        self.file_name_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.file_name_label.setText("")
        self.file_name_label.setObjectName("file_name_label")

        self.h2.addWidget(self.open_file_btn)
        self.h2.addWidget(self.file_name_label)

        self.verticalLayout.addLayout(self.h1)
        self.verticalLayout.addLayout(self.h2)
        #2nd vertical layout
        self.v3 = QtWidgets.QVBoxLayout()
        self.v3.setObjectName("v3")
        self.v3.setContentsMargins(5,5,5,5)

        self.code_box = QtWidgets.QPlainTextEdit(self.verticalLayoutWidget)
        self.code_box.setObjectName("code_box")
        self.code_box.setFont(font_code)
        self.metrics=QtGui.QFontMetrics(font_code)
        self.code_box.setTabStopWidth(self.metrics.width(' ')*4)
        
        self.code_box_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.code_box_label.setFont(font_calibri_12)
        self.code_box_label.setObjectName("code_box_label")
        
        self.paste_btn= QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.paste_btn.setObjectName("paste_btn")
        self.paste_btn.clicked.connect(self.paster)
                
        self.v3.addWidget(self.code_box_label)
        self.v3.addWidget(self.code_box)
        self.v3.addWidget(self.paste_btn)

        self.verticalLayout.addLayout(self.v3)

        self.url_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.url_label.setFont(font_calibri_14)
        self.url_label.setObjectName("url_label")
        self.url_label.setSizePolicy(QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum))
        
        self.url_text = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.url_text.setFont(font_calibri_14)
        self.url_text.setText("")
        self.url_text.setObjectName("url_text")

        self.h3 = QtWidgets.QHBoxLayout()
        self.h3.setObjectName("h3")

        self.h3.addWidget(self.url_label)
        self.h3.addWidget(self.url_text)
        self.h3.setContentsMargins(5,5,5,5)

        self.verticalLayout.addLayout(self.h3)       
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
        MainWindow.setWindowTitle(_translate("MainWindow", ""))
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
        self.fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","All Files (*)", options=options)
        if self.fileName!="":
            self.file_name_label.setText(self.fileName)
            data=auto_pastebin.read_file(self.fileName)
            self.code_box.setPlainText(data)
    def paster(self):
        data=""
        if self.username_input_field.text()=="":
            data= {
	            'poster':getpass.getuser(),
	            'syntax':'text',
	            'content': self.code_box.toPlainText()
	        }
        else:
             data= {
	            'poster':self.username_input_field.text(),
	            'syntax':'text',
	            'content': self.code_box.toPlainText()
	        }
        
        response=auto_pastebin.post_req(data,"https://pastebin.ubuntu.com/")
        if response.ok:
           self.url_text.setText(response.url)
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
