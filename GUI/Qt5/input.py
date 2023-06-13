import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg

class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()
        #add title
        self.setWindowTitle("Hello Eswar")
        #setting layout for arrangements (grid)
        self.setLayout(qtw.QVBoxLayout())#vertical layout QVBox (QHBox for horizontal layout)
        
        #creating a label
        my_label = qtw.QLabel("Hello  bro")
        self.layout().addWidget(my_label)
        #changing the font size of label(for this imported second line "Qtgui")
        my_label.setFont(qtg.QFont('orbitron', 18))
        
        #creating an empty box
        my_entry = qtw.QLineEdit()
        my_entry.setObjectName("Name feild")
        my_entry.setText("")
        self.layout().addWidget(my_entry)

        #creating a combo box
        my_combo = qtw.QComboBox(self, editable =True)
        #adding items to combo box
        my_combo.addItem("Eswar", "Your name")
        my_combo.addItem("Rao","Rao" )
        my_combo.addItem("python", qtw.QTabWidget)
        my_combo.addItem("Photography", "Sony A7R3")
        my_combo.addItems(["one","two","three"])
        my_combo.insertItem(2,"Eswara Rao","Eswararao" )#will adds the item as third item (index 2)
        #put combobox on screen
        self.layout().addWidget(my_combo)

        #variable input number change (calling spin box)
        my_spin = qtw.QSpinBox(self, value=0, maximum=100,minimum=0,singleStep=5, prefix="At  ",suffix="th Position")
        self.layout().addWidget(my_spin)


        #creating a button 
        my_button = qtw.QPushButton("click me!",clicked = lambda: press_it())
        self.layout().addWidget(my_button)
        self.show()

        def press_it():
            #add name to label
            # my_label.setText(f'hii{my_entry.text()}')
            my_label.setText(f'You selected  {my_combo.currentData()}!')
            #clear the entry box
            my_entry.setText("")


app = qtw.QApplication([])
mw = MainWindow()

#running the app
app.exec_()