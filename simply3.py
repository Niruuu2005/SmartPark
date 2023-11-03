from pathlib import Path
from tkinter import Frame, Label, Tk
from tkVideoPlayer import TkinterVideo

root=Tk()

loc = Path(__file__).parent.resolve()
loc = str(loc) + "\\"

frame = Frame(root, bg="beige")

def mainscr():

    main_id = Label(frame, text="Parking SPAN", font=("Time New Roman", 15))
    des = Label(frame, text="Park  with  Trust, have  FAITH.",
                font=("Times New Roman", 12))

    vid = TkinterVideo(frame, scaled=True)
    vid.load(loc + "giff.mp4")

    main_id.grid(row=0, column=0, pady=1)
    des.grid(row=1, column=0, pady=2, )
    vid.grid(row=2, column=0)

    frame.pack(side='left', pady=10, padx=300)

    vid.play()

    vid.after(180000, vid)
    
mainscr()

root.mainloop()