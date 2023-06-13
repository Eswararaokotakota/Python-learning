import PyQt5.QtWidgets as qtw


class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Eswar")
        self.setLayout(qtw.QHBoxLayout())

#----------------------- spin box -----------------------------
        spin_box = qtw.QSpinBox(self, minimum=0, maximum=100, value=0, singleStep=5.05, prefix="At  ",suffix=" Position")
        self.layout().addWidget(spin_box)
#------------------------------------------------------------------

        self.show()

app = qtw.QApplication([])
mw = MainWindow()
app.exec_()