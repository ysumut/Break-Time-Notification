from PyQt5 import QtCore, QtGui, QtWidgets
import os
from shutil import copyfile


class Ui_MainWindow(object):
    def __init__(self):
        
        self.counterPath = 'C:/Users/'+ os.getlogin() +'/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup/bg_counter.vbs'
        self.pythonPath = ""
    
    def setupUi(self, MainWindow):
        self.MainWindow = MainWindow
        self.MainWindow.setObjectName("MainWindow")
        self.MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(self.MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.submitButton = QtWidgets.QPushButton(self.centralwidget)
        self.submitButton.setGeometry(QtCore.QRect(30, 400, 91, 31))
        self.submitButton.setObjectName("submitButton")
        self.submitButton.clicked.connect(self.onClick)
        
        self.dialogButton = QtWidgets.QPushButton(self.centralwidget)
        self.dialogButton.setGeometry(QtCore.QRect(300, 280, 91, 31))
        self.dialogButton.setObjectName("dialogButton")
        self.dialogButton.clicked.connect(self.openFileNameDialog)
        
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(240, 20, 341, 61))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(30, 130, 400, 20))
        self.checkBox.setObjectName("checkBox")
        self.checkBoxControl()
        
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(85, 207, 71, 31))
        self.textEdit.setObjectName("textEdit")
        
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 200, 50, 41))
        self.label_2.setStyleSheet("font-size: 20px")
        self.label_2.setObjectName("label_2")
        
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 275, 281, 41))
        self.label_3.setStyleSheet("font-size: 20px")
        self.label_3.setObjectName("label_3")
        
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(160, 200, 281, 41))
        self.label_4.setStyleSheet("font-size: 20px")
        self.label_4.setObjectName("label_4")
        
        self.dialogLabel = QtWidgets.QLabel(self.centralwidget)
        self.dialogLabel.setGeometry(QtCore.QRect(30, 320, 500, 41))
        self.dialogLabel.setStyleSheet("color: rgb(255,0,0)")
        self.dialogLabel.setObjectName("dialogLabel")
        
        self.MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(self.MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        self.MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(self.MainWindow)
        self.statusbar.setObjectName("statusbar")
        self.MainWindow.setStatusBar(self.statusbar)
        
        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self.MainWindow)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.MainWindow.setWindowTitle(_translate("MainWindow", "Break Time"))
        self.submitButton.setText(_translate("MainWindow", "Submit"))
        self.dialogButton.setText(_translate("MainWindow", "Browse File"))
        self.label.setText(_translate("MainWindow", "Break Time Notification"))
        self.checkBox.setText(_translate("MainWindow", "When the computer turns on, let the counter start automatically?"))
        self.label_2.setText(_translate("MainWindow", "Every"))
        self.label_3.setText(_translate("MainWindow", "Select your python.exe file: "))
        self.label_4.setText(_translate("MainWindow", "minute, the counter run."))
        self.dialogLabel.setText(_translate("MainWindow", self.pythonPath))

    def onClick(self):
        if((self.pythonPath == "") or (self.textEdit.toPlainText() == "")):
            self.warningMessage()
            return
        
        
        dir_path = "C:/Users/{}/Break-Time-Notification".format(os.getlogin())
        
        with open("background/bg_counter.vbs", "w") as file:
            source = 'CreateObject("Wscript.Shell").Run "{}\\background\\bg_counter.bat",0,True'.format(os.getcwd())
            file.write(source)
        
        
        minute = self.textEdit.toPlainText()
        if(self.checkBox.isChecked()):
            copyfile('background/bg_counter.vbs', self.counterPath)
        else:
            if os.path.exists(self.counterPath):
                os.remove(self.counterPath)
            
            
        if not os.path.exists(dir_path):
            os.mkdir(dir_path)  # firstly, create a directory
            
        copyfile('background/break.ico', dir_path + '/break.ico')
        
        with open(dir_path + "/minute.txt", "w") as file:
            file.write(minute)
        
        
        with open("background/bg_counter.bat", 'w') as file:
            file.write(self.pythonPath + " " + "{}\\background\\background_counter.py".format(os.getcwd()))
        
        
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.setText("Successful")
        msg.setInformativeText("When the computer restarts, the counter will start running.")
        msg.setWindowTitle("Information")
        msg.exec_()
    
    
    def checkBoxControl(self):
        if os.path.exists(self.counterPath):
            self.checkBox.setChecked(True)
            
            
    def openFileNameDialog(self):
        fileName = QtWidgets.QFileDialog.getOpenFileName()
        self.pythonPath = fileName[0]
        self.retranslateUi()
        
    
    def warningMessage(self):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Warning)
        msg.setText("Look Again")
        msg.setInformativeText("There are missing things.")
        msg.setWindowTitle("Warning")
        msg.exec_()
        
    
        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())