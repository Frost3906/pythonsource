from tkinter import * 
from tkinter import messagebox

def clickLeft(event):
    messagebox.showinfo("토끼토끼")

window = Tk()
window.geometry("400x400")

photo = PhotoImage(file="./resource/rabbit.gif")
label = Label(window, image=photo)
label.bind("<Button-1>",clickLeft)

label.pack(expand=1, anchor=CENTER)
window.mainloop()