from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(350, 549)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.output_label = QtWidgets.QLabel(self.centralwidget)
        self.output_label.setGeometry(QtCore.QRect(4, 5, 341, 71))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.output_label.setFont(font)
        self.output_label.setFrameShape(QtWidgets.QFrame.Box)
        self.output_label.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.output_label.setLineWidth(3)
        self.output_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.output_label.setObjectName("output_label")
        self.percentButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda : self.press_it("%"))
        self.percentButton.setGeometry(QtCore.QRect(10, 80, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.percentButton.setFont(font)
        self.percentButton.setObjectName("percentButton")
        self.clearButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda : self.press_it("C"))
        self.clearButton.setGeometry(QtCore.QRect(100, 80, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.clearButton.setFont(font)
        self.clearButton.setObjectName("clearButton")
        self.arrowButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda : self.remove())
        self.arrowButton.setGeometry(QtCore.QRect(190, 80, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.arrowButton.setFont(font)
        self.arrowButton.setObjectName("arrowButton")
        self.devideButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda : self.press_it("/"))
        self.devideButton.setGeometry(QtCore.QRect(270, 80, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.devideButton.setFont(font)
        self.devideButton.setObjectName("devideButton")
        self.mulButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda : self.press_it("x"))
        self.mulButton.setGeometry(QtCore.QRect(270, 164, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.mulButton.setFont(font)
        self.mulButton.setObjectName("mulButton")
        self.Button_9 = QtWidgets.QPushButton(self.centralwidget, clicked = lambda : self.press_it("9"))
        self.Button_9.setGeometry(QtCore.QRect(190, 164, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Button_9.setFont(font)
        self.Button_9.setObjectName("Button_9")
        self.Button_7 = QtWidgets.QPushButton(self.centralwidget, clicked = lambda : self.press_it("7"))
        self.Button_7.setGeometry(QtCore.QRect(10, 164, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Button_7.setFont(font)
        self.Button_7.setObjectName("Button_7")
        self.Button_8 = QtWidgets.QPushButton(self.centralwidget, clicked = lambda : self.press_it("8"))
        self.Button_8.setGeometry(QtCore.QRect(100, 164, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Button_8.setFont(font)
        self.Button_8.setObjectName("Button_8")
        self.subButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda : self.press_it("-"))
        self.subButton.setGeometry(QtCore.QRect(270, 250, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.subButton.setFont(font)
        self.subButton.setObjectName("subButton")
        self.Button_4 = QtWidgets.QPushButton(self.centralwidget, clicked = lambda : self.press_it("4"))
        self.Button_4.setGeometry(QtCore.QRect(10, 250, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Button_4.setFont(font)
        self.Button_4.setObjectName("Button_4")
        self.Button_6 = QtWidgets.QPushButton(self.centralwidget, clicked = lambda : self.press_it("6"))
        self.Button_6.setGeometry(QtCore.QRect(190, 250, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Button_6.setFont(font)
        self.Button_6.setObjectName("Button_6")
        self.Button_5 = QtWidgets.QPushButton(self.centralwidget, clicked = lambda : self.press_it("5"))
        self.Button_5.setGeometry(QtCore.QRect(100, 250, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Button_5.setFont(font)
        self.Button_5.setObjectName("Button_5")
        self.Button_2 = QtWidgets.QPushButton(self.centralwidget, clicked = lambda : self.press_it("2"))
        self.Button_2.setGeometry(QtCore.QRect(100, 340, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Button_2.setFont(font)
        self.Button_2.setObjectName("Button_2")
        self.Button_3 = QtWidgets.QPushButton(self.centralwidget, clicked = lambda : self.press_it("3"))
        self.Button_3.setGeometry(QtCore.QRect(190, 340, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Button_3.setFont(font)
        self.Button_3.setObjectName("Button_3")
        self.Button_1 = QtWidgets.QPushButton(self.centralwidget, clicked = lambda : self.press_it("1"))
        self.Button_1.setGeometry(QtCore.QRect(10, 340, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Button_1.setFont(font)
        self.Button_1.setObjectName("Button_1")
        self.plusButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda : self.press_it("+"))
        self.plusButton.setGeometry(QtCore.QRect(270, 340, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.plusButton.setFont(font)
        self.plusButton.setObjectName("plusButton")
        self.Button_0 = QtWidgets.QPushButton(self.centralwidget, clicked = lambda : self.press_it("0"))
        self.Button_0.setGeometry(QtCore.QRect(100, 420, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Button_0.setFont(font)
        self.Button_0.setObjectName("Button_0")
        self.dotButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda : self.press_it("."))
        self.dotButton.setGeometry(QtCore.QRect(190, 420, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.dotButton.setFont(font)
        self.dotButton.setObjectName("dotButton")
        self.plusminusButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda : self.press_it("+/-"))
        self.plusminusButton.setGeometry(QtCore.QRect(10, 420, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.plusminusButton.setFont(font)
        self.plusminusButton.setObjectName("plusminusButton")
        self.equalsButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda : self.math())
        self.equalsButton.setGeometry(QtCore.QRect(270, 420, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.equalsButton.setFont(font)
        self.equalsButton.setObjectName("equalsButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 350, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
  
     #--------------------------------------------------------------
    def math(self):
        screen = self.output_label.text()
        try:
            #do the math
            answer = eval(screen)
            #O/P ans to the screen
            self.output_label.setText(str(answer))
        except:
            self.output_label.setText(str("Error....!"))
     #--------------------------------------------------------------


     #---------------------del(<<)--------------------------------------
    def remove(self):
        #grab whats on the screen already
        screen = self.output_label.text()
        #Remove last item in the list/string
        screen = screen[:-1]
        #output back to the screen
        self.output_label.setText(screen)
     #--------------------------------------------------------------


     #---------------Dot------------------------------------------- 
    def dot(self):
        screen = self.output_label.text()
        self.output_label.setText(f'{screen}.')
     #--------------------------------------------------------------
   

     #---------------------clear-------------------------------------  
    def press_it(self, pressed):
        if pressed == "C":
            self.output_label.setText("0")
        else:
            if self.output_label.text() == "0": #here we are clearing the initial 0 from our number
                self.output_label.setText("")
            #concatinate the pressed button with previous one
            self.output_label.setText(f'{self.output_label.text()}{pressed}')
     #------------------------------------------------------------------   
      

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Calculator"))
        self.output_label.setText(_translate("MainWindow", "0"))
        self.percentButton.setText(_translate("MainWindow", "%"))
        self.clearButton.setText(_translate("MainWindow", "c"))
        self.arrowButton.setText(_translate("MainWindow", "<<"))
        self.devideButton.setText(_translate("MainWindow", "/"))
        self.mulButton.setText(_translate("MainWindow", "x"))
        self.Button_9.setText(_translate("MainWindow", "9"))
        self.Button_7.setText(_translate("MainWindow", "7"))
        self.Button_8.setText(_translate("MainWindow", "8"))
        self.subButton.setText(_translate("MainWindow", "-"))
        self.Button_4.setText(_translate("MainWindow", "4"))
        self.Button_6.setText(_translate("MainWindow", "6"))
        self.Button_5.setText(_translate("MainWindow", "5"))
        self.Button_2.setText(_translate("MainWindow", "2"))
        self.Button_3.setText(_translate("MainWindow", "3"))
        self.Button_1.setText(_translate("MainWindow", "1"))
        self.plusButton.setText(_translate("MainWindow", "+"))
        self.Button_0.setText(_translate("MainWindow", "0"))
        self.dotButton.setText(_translate("MainWindow", "."))
        self.plusminusButton.setText(_translate("MainWindow", "+/-"))
        self.equalsButton.setText(_translate("MainWindow", "="))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())