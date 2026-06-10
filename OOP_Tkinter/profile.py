from tkinter import *
from tkinter import ttk
from tkinter import font
from tkinter import PhotoImage

class Profile:
    def __init__(self, root):

        root.title("Luigi Ryan M. Parzuelo")

        mainframe = ttk.Frame(root)
        mainframe.grid(column=0, row=0)
        
        mainText = ttk.Label(mainframe, text="Luigi the Nigga", compound='center')
        mainText.grid(column=0, row=0, columnspan=3)

        introduction = ttk.Button(mainframe, text="Introduction", padding=(5, 10, 5, 10))
        introduction.grid(column=2, row=2)

          




root = Tk()
Profile(root)
root.mainloop()