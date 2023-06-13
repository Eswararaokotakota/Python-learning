import PyQt5.QtWidgets as qtw


class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Eswar")
        self.setLayout(qtw.QHBoxLayout())

#----------------------- Drop Down -----------------------------
        Drop_down = qtw.QComboBox(self)
        Drop_down.addItem("Eswar", "Yeah! Eswar")
        Drop_down.addItem("Rao", "Yeah! Rao")
        Drop_down.addItem("Pyton", "Yeah! Python")
        Drop_down.addItem("opencv", "Yeah! OpenCv")
        Drop_down.addItem("Qt5", "Yeah! Qt5")
        self.layout().addWidget(Drop_down)
#---------------------------------------------------------------

        self.show()

app = qtw.QApplication([])
mw = MainWindow()
app.exec_()