from tkinter import*
root = Tk()

e = Entry(root, width =50, bg = "yellow", fg="black")#creates a input feild
e.pack()
e.insert(0,"Enter your name:")#will initially place this text in the feild


def clicking():
    hello = "Hello"
    mylabel = Label(root, text=hello+e.get())#e.get(will get the data entered in the input feild)
    mylabel.pack()
    print("Hei.... stopclicking!")

myButton = Button(root, text="Clickme!", padx=50,pady=25, command=clicking, fg="Blue", bg="skyblue") #padx&y are sizes [fg,text color] [bg = backgriund color]
myButton.pack()



root=mainloop()


