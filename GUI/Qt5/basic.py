import PyQt5.QtWidgets as qtw


class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Eswar")
        self.setLayout(qtw.QHBoxLayout())
        #Adding a button
        button = qtw.QPushButton("Iam a button", clicked = lambda: pressed())  #\\\\\\\\\\
        self.layout().addWidget(button)           #\\\\\\\\\\  Just two lines to add abutton
       
        def pressed():
            button.setText("Hei pressed")  #just changed the text in the Button
        self.show()

app = qtw.QApplication([])
mw = MainWindow()
app.exec_()