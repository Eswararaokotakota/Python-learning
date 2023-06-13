from tkinter import*

def clicking():
    mylabel = Label(root, text="Buton is just clicked!")
    mylabel.pack()
    print("Hei:[ stopclicking!!!!!!!!!!!")

root = Tk()

myButton = Button(root, text="Clickme!", padx=50,pady=25, command=clicking, fg="Blue", bg="skyblue") #padx&y are sizes [fg,text color] [bg = backgriund color]
myButton.pack()

root.mainloop()