from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from todo_ui import Ui_MainWindow
import pymysql
from datetime import date


class todo_ui_window(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(todo_ui_window,self).__init__()
        # QMainWindow.__init__(self)
        self.setupUi(self)
        self.db_connection()
        self.today_date = date.today()
        self.today_date = self.today_date.strftime("%d-%m-%Y")
        self.date.setText(str(self.today_date))
        self.ADD.clicked.connect(self.add)
        self.clear_list.clicked.connect(self.clear_all)
        self.Remove.clicked.connect(self.remove)
        self.history.clicked.connect(self.show_history)
        self.clear_history.clicked.connect(self.clearing_history)
        self.items_list=[]
        self.history_list=[]
         
        
    def db_connection(self): 
        self.todo_db = pymysql.connect(host="localhost",user="root", passwd="delhi123", db="to_do_database" )
        print("sql Connected")
        self.cursor = self.todo_db.cursor()
        
    def add_to_database(self, command, data):
        # todo_db = pymysql.connect(host="localhost",user="root", passwd="delhi123", db="to_do_database" )
        # print("sql Connected")
        # self.cursor = todo_db.cursor()
        self.cursor.execute("use to_do_database")
        self.cursor.execute(command, data)
        self.todo_db.commit()
        
    
         
    def add(self): 
        if not self.lineEdit.text(): #If there is no text in the input feild the it will pops up ("Error message")
            error_dialog = QtWidgets.QMessageBox()
            error_dialog.setWindowTitle("Error..")
            error_dialog.setIcon(QMessageBox.Critical)
            error_dialog.setText('Please write something..!')
            x=error_dialog.exec_() #To display message box we should write this line.
        else:    
            self.text = self.lineEdit.text()
            print(self.text)
            command = ("insert into todo_data values(%s)" )
            data = self.lineEdit.text()
            self.add_to_database(command, data)
            self.items_list.append(data)
            self.listWidget.addItems([self.items_list[-1]])
            self.lineEdit.clear()
            
            
    def remove(self):
        # task= self.listWidget.get(self.listWidget.curselection())
        # print("remove")
        selection = self.listWidget.currentRow()
        if selection == -1:
            print("Please select something to delete")
            error_dialog = QtWidgets.QMessageBox()
            error_dialog.setWindowTitle("Warning..")
            error_dialog.setIcon(QMessageBox.Warning)
            error_dialog.setText('Please select a task to remove.')
            x=error_dialog.exec_()
        self.listWidget.takeItem(selection)
        # print(selection)
        
    
    def clear_all(self):
        print("clear")
        self.listWidget.clear()
        error_dialog = QtWidgets.QMessageBox()
        error_dialog.setWindowTitle("ToDo List")
        error_dialog.setIcon(QMessageBox.Information)
        error_dialog.setText('List Cleared Successfully..!')
        x=error_dialog.exec_()
        
    def show_history(self):
        self.cursor.execute("select * from todo_data")
        history_data = self.cursor.fetchall()
        for i in history_data:
            self.history_list.append(i[0])
        self.listWidget.clear()
        # for j in self.history_list
        self.listWidget.addItems(self.history_list)
        self.lineEdit.clear()
    
    def clearing_history(self):
        self.cursor.execute("TRUNCATE TABLE todo_data")
        self.history_list.clear()
        self.listWidget.clear()
        print("Done..!")
        
        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    # app.setStyle(QStyleFactory.create("Fusion"))
    todo_gui = todo_ui_window()
    todo_gui.show()
    sys.exit(app.exec_())
    
    