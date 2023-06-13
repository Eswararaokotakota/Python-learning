# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'translator_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(983, 600)
        MainWindow.setStyleSheet("background-color:rgb(255, 255, 255)")
        MainWindow.setWindowIcon(QtGui.QIcon("translate.png"))
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.logo = QtWidgets.QPushButton(self.centralwidget)
        self.logo.setGeometry(QtCore.QRect(30, 20, 30, 30))
        self.logo.setObjectName("translate_icon")
        # self.logo.setIcon(QtGui.QIcon("translate.png"))
        self.logo.setStyleSheet("background-image: url('translate.png');")
        
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(430, 10, 200, 41))
        self.label.setStyleSheet("font: 10 20pt;color:blue;\n")
        self.label.setObjectName("label")
        
        self.arrow = QtWidgets.QPushButton(self.centralwidget)
        self.arrow.setGeometry(QtCore.QRect(452, 65, 100, 100))
        self.arrow.setObjectName("translate_icon")
        self.arrow.setIcon(QtGui.QIcon("right-arrow.png"))
        self.arrow.setStyleSheet("border:none;")
        
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(50, 100, 430, 31))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("English")
        self.comboBox.setStyleSheet("color:blue;font: 10 10pt;background-color:#f2f7fc;border: none;border-radius: 5px;\n""")
        # self.comboBox.addItem("Telugu")
        # self.comboBox.addItem("Hindi")
        
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(520, 100, 430, 31))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("Telugu")
        self.comboBox_2.addItem("Hindi")
        self.comboBox_2.addItem("English")
        self.comboBox_2.setStyleSheet("color:blue;font: 10 10pt ;background-color:#f2f4f5;border:none;border-radius: 5px;\n""")
        
        self.textBrowser = QtWidgets.QTextEdit(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(50, 140, 431, 371))
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser.setStyleSheet("""font: 10 15pt;background-color:#f2f7fc;border-radius: 10px;\n""")

        self.textBrowser_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(520, 140, 431, 371))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.textBrowser_2.setStyleSheet("""font: 10 15pt;background-color:#f2f4f5;border-radius: 10px;\n""")
        
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 50, 981, 21))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.translate_button = QtWidgets.QPushButton(self.centralwidget)
        self.translate_button.setGeometry(QtCore.QRect(450, 70, 100, 20))
        self.translate_button.setObjectName("Translate_button")
        self.translate_button.setVisible(False)
        
        self.speak_1 = QtWidgets.QPushButton(self.centralwidget)
        self.speak_1.setGeometry(QtCore.QRect(220, 530, 50, 30))
        self.speak_1.setStyleSheet("""font: 10 20pt;\n""")
        self.speak_1.setIcon(QtGui.QIcon("wave-sound.png"))
        self.speak_1.setStyleSheet("""QPushButton{background-color:skyblue;border:none;border-radius:5px;}
                                   QPushButton:hover{background-color:#56b5f0;}""")
        
        self.speak_2 = QtWidgets.QPushButton(self.centralwidget)
        self.speak_2.setGeometry(QtCore.QRect(720, 530, 50, 30))
        self.speak_2.setObjectName("Speak2")
        self.speak_2.setStyleSheet("font: 10 20pt;\n")
        self.speak_2.setIcon(QtGui.QIcon("wave-sound.png"))
        self.speak_2.setStyleSheet("""QPushButton{background-color:skyblue;border:none;border-radius:5px;}
                                   QPushButton:hover{background-color:#56b5f0;}""")
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 983, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        
        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Eswar's Translator"))
        self.label.setText(_translate("MainWindow", "Translator"))
        self.translate_button.setText(_translate("MainWindow", "Translate"))
        # self.speak_1.setText(_translate("MainWindow", "speak"))
        # self.speak_2.setText(_translate("MainWindow", "speak"))
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())