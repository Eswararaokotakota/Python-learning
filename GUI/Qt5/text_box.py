import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg

class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Eswar")
        self.setLayout(qtw.QHBoxLayout())

#----------------------- Text box -----------------------------
        text_box= qtw.QTextEdit(self)
        self.layout().addWidget(text_box)
#------------------------------------------------------------------

        self.show()

app = qtw.QApplication([])
mw = MainWindow()
app.exec_()