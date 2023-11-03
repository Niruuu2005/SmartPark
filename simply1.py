from pathlib import Path
from tkinter import *


root=Tk()
# location
loc = Path(__file__).parent.resolve()
loc = str(loc) + "\\"

def ico_site(t):
    t.title("Parking SPAN")
    t.iconbitmap(loc + "gui.ico")

    t.geometry('800x500')
    t.configure(background="beige")
    t.attributes("-fullscreen", True)
    
