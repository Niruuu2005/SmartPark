
from PIL import Image, ImageTk
from pathlib import Path
from time import strftime
from tkinter import Canvas, Label, Tk

root=Tk()

loc = Path(__file__).parent.resolve()
loc = str(loc) + "\\"


a = Image.open(loc + "icoon.png")
img_ = ImageTk.PhotoImage(a)

def margin(t,i):
    c = Canvas(t, bg="Bisque", border=0)
    c.pack(anchor='n', fill='x')
    
    
    img__ = Label(c, image=i, bg="Bisque")
    img__.pack(anchor="n", side='left')

    b = Label(c, text="Parking SPAN", font=("", 15), bg="Bisque")
    b.pack(side='left', anchor='n', pady=50)

    labeli = Label(c, font=("", 13), bg="Bisque")
    labeli.pack(anchor="se", pady=10)

    labelo = Label(c, font=("", 13), bg="Bisque")
    labelo.pack(anchor="se", pady=10)

    def date_dis():

        d1 = strftime("DATE :- %d/%m/%Y")
        labelo.config(text=d1)
        labelo.after(86400000, date_dis)

    def time():

        d2 = strftime("TIME :- %I : %M : %S %p ")
        labeli.config(text=d2)
        labeli.after(1000, time)

    date_dis()
    time()
