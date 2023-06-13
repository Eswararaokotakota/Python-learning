from tkinter import*

root = Tk()

mylabel1 = Label(root, text="hello Eswar")
mylabel2 = Label(root, text="pandagoooooo")

#putting on the screen
mylabel1.grid(row=0, column=0)#will stay left top
mylabel2.grid(row=1, column=0)#will stay down to the above texts

root.mainloop()