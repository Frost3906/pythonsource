from tkinter import *

window = Tk()

photo1 = PhotoImage(file="./resource/cat2.gif")
label = Label(window, image=photo1)

photo2 = PhotoImage(file="./resource/dog2.gif")
lable2 = Label(window, image=photo2)


label.pack(side=LEFT)
lable2.pack(side=LEFT)

window.mainloop()
