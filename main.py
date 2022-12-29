import makeInstuctions

import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd

# create the root window
root = tk.Tk()
root.title('Pancake Gcode Generator')
root.resizable(False, False)
root.geometry('350x500')
varColor = tk.IntVar()

def select_file():
    filetypes = (('text files', '*.jpg'),)

    filename = fd.askopenfilename(
        title='Open a .jpg',
        initialdir='/',
        filetypes=filetypes)    
    makeInstuctions.makeInstuctions(filename, 152.4, 152.4, v.get())


# open button
open_button = tk.Button(
    root,
    text='Open a File',
    width=30,
    height=20,
    bg='white',
    command=select_file
)

#the color picker
v = tk.IntVar()
v.set(0)  # initializing the choice, i.e. Python

colors = [("Black", 0), ("White", 255), ("Gray", 127)]

def ShowChoice():
    print(v.get())

for colors, val in colors:
    tk.Radiobutton(root, 
                   text=colors,
                   padx = 20, 
                   variable=v, 
                   command=ShowChoice,
                   value=val).grid(row = val + 2,sticky='W')

# lable
lable = tk.Label(root, text="Gavin's Great G-Code Generator!", font='Times 18')

open_button.grid(column=0, row=1, padx=10, pady=20)
lable.grid(column=0, row=0, padx=10)

#cBlack.grid(column=0, row=6, padx=40, sticky='W')
#cWhite.grid(column=0, row=7, padx=40,sticky='W')
#cGray.(column=0, row=8, padx=40,sticky='W')


# run the application
root.mainloop()