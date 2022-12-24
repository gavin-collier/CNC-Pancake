import functools
import makeGcode

import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd

# create the root window
root = tk.Tk()
root.title('Tkinter Open File Dialog')
root.resizable(False, False)
root.geometry('350x500')

def select_file():
    filetypes = (('text files', '*.jpg'),)

    filename = fd.askopenfilename(
        title='Open a .jpg',
        initialdir='/',
        filetypes=filetypes)    
    makeGcode.generate_Gcode(filename)


# open button
open_button = tk.Button(
    root,
    text='Open a File',
    width=30,
    height=20,
    bg='white',
    command=select_file
)

# lable
lable = tk.Label(root, text="Gavin's Great G-Code Generator!", font='Times 18')

open_button.grid(column=0, row=5, padx=10, pady=30)
lable.grid(column=0, row=0, padx=10, pady=10)

# run the application
root.mainloop()