#좋아하는 동물 투표하는 프로그램

from tkinter import *

def myFunc():
    if rdo.get() == 1:
        label2.configure(image=photo1)
    elif rdo.get() == 2:
        label2.configure(image=photo2)
    else :
        label2.configure(image=photo3)



window = Tk()
window.geometry("500x400")
window.title("애완동물 선택하기")

rdo = IntVar()

label = Label(font=("궁서체",30),fg="red",text="좋아하는 동물 투표")
label2 = Label(window)
photo1 = PhotoImage(file="./resource/dog2.gif")
photo2 = PhotoImage(file="./resource/cat2.gif")
photo3 = PhotoImage(file="./resource/rabbit.gif")


rb1 = Radiobutton(window, text="강아지", variable = rdo, value = 1)
rb2 = Radiobutton(window, text="고양이", variable = rdo, value = 2)
rb3 = Radiobutton(window, text="토끼", variable = rdo, value = 3)

btn = Button(window, text="사진 보기",command=myFunc)

label.pack()
rb1.pack()
rb2.pack()
rb3.pack()
btn.pack()
label2.pack()

window.mainloop()

