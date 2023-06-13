from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from transllator_ui import Ui_MainWindow
from datetime import date
from googletrans import Translator
from elevenlabslib import *

 
class Trans(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(Trans,self).__init__()
        self.setupUi(self)
        try:
            self.api = ElevenLabsUser("2a4e9c5178c68739db794e528c97cf0c")
            self.voice =self.api.get_voices_by_name("Sam")[0]
        except:
            self.label.setText("Oops... No Internet!")
            self.label.setStyleSheet("color:red;font:20 20px;")
                
        self.textBrowser.textChanged.connect(self.translating)
        self.comboBox_2.currentIndexChanged.connect(self.translating)
        self.speak_1.clicked.connect(self.speaking1)
        self.speak_2.clicked.connect(self.speaking2)
        
    def translating(self):
        self.text1 = self.textBrowser.toPlainText()
        self.text2 = self.textBrowser_2.toPlainText()
        self.language_selection1 = self.comboBox.currentText()
        self.language_selection2 = self.comboBox_2.currentText()
        translater = Translator()
        if self.language_selection2 == "English":
            language = "en"
        elif self.language_selection2 == "Hindi":
            language = "hi"      
        elif self.language_selection2 == "Telugu":
            language = "te"    
        
        my_text= translater.translate(self.text1, dest=language)
        self.textBrowser_2.clear()
        self.textBrowser_2.setText(my_text.text)
        
    def speaking1(self):
        self.text2 = self.textBrowser_2.toPlainText()
        self.voice.generate_and_play_audio(self.text1,playInBackground=False)
        
    def speaking2(self):
        self.text2 = self.textBrowser_2.toPlainText()
        self.voice.generate_and_play_audio(self.text2,playInBackground=False)
       
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    # app.setStyle(QStyleFactory.create("Fusion"))
    todo_gui = Trans()
    todo_gui.show()
    sys.exit(app.exec_())