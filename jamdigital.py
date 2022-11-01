from tkinter import *
from tkinter.ttk import *
from time import strftime

atas = Tk()
atas.title("Jam Digital")


def jam():
    text = strftime('%H:%M:%S %p')
    Label.config(text=text)
    Label.after(1000, jam)


lab = Label(atas, font=('digital-10', 200, 'bold'),
            background='black', foreground='yellow')
lab.pack(anchor='center')
jam()
mainloop()
