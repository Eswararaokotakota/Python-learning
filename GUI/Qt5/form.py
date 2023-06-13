import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg

class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Eswar")
        # self.setLayout(qtw.QHBoxLayout())

#----------------------- Form -----------------------------
        form_layout = qtw.QFormLayout()
        self.setLayout(form_layout)

        lable_1 = qtw.QLabel("This a label")
        lable_1.setFont(qtg.QFont("Helvetica", 24))
        
        #adding things
        f_name = qtw.QLineEdit(self)
        l_name = qtw.QLineEdit(self)

        #ading lable to App
        form_layout.addRow(lable_1)
        form_layout.addRow("First Name", f_name)
        form_layout.addRow("Last Name", l_name)
        form_layout.addRow(qtw.QPushButton("Click me!", clicked= lambda: pressed()))
       
#----------------------------------------------------------
        self.show()

        def pressed():
            lable_1.setText(f'Yohoooo...! {f_name.text()} {l_name.text()}')

app = qtw.QApplication([])
mw = MainWindow()
app.exec_()