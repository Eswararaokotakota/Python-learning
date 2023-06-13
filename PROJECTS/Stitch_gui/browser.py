# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'browse.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.file = None
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(887, 542)
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        MainWindow.setFocusPolicy(QtCore.Qt.NoFocus)
        MainWindow.setStyleSheet("background-color:rgb(0, 170, 255)")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Browse = QtWidgets.QPushButton(self.centralwidget)
        self.Browse.setGeometry(QtCore.QRect(380, 220, 151, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.Browse.setFont(font)
        self.Browse.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Browse.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.Browse.setStyleSheet("background:rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"")
        self.Browse.setAutoDefault(False)
        self.Browse.setDefault(False)
        self.Browse.setFlat(False)
        self.Browse.setObjectName("Browse")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(390, 280, 151, 41))
        self.label.setStyleSheet("color:rgb(255, 255, 255)")
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 887, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Browse.setText(_translate("MainWindow", "Browse"))
        self.label.setText(_translate("MainWindow", "(Select calibration images folder)"))
     
    #------------------------------Browse Button---------------------------#
    def Browse_folder(self):
        print("Hey stop pressing!....")
        # self.file = QFileDialog.getExistingDirectory()
        print(self.file)
        
        # print(file)
        # return self.file
    # def call_warp():
        
        # main_stitch = warp_stitch()
        # main_stitch.run_stitch_code()s

        # path = "E:\\Coding\\Python\\projects\\Stitch_gui"
        # txt_file = open(path+"folderpath.txt","w")
        # data = input("Type something :  ")
        # txt_file.write(data+"\n")
        # txt_file.close()

    # def folderpath(self):
    #     print("ghasd")
    #     return file
    

    #----------------------------------------------------------------------#

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

