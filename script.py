from tkinter import *

window= Tk()

l1 = Label(window, text="Title")
l1.grid(row=0, column=0)

l2 = Label(window, text="Title")
l2.grid(row=0, column=2)

l3 = Label(window, text="Title")
l3.grid(row=1, column=0)

l4 = Label(window, text="Title")
l4.grid(row=1, column=4)


window.mainloop()

