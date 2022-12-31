import makeInstuctions

from tkinter import *
import tkinter as tk
from tkinter import ttk
import tkinter.font as font
from tkinter import filedialog as fd

# create the root window
root = tk.Tk()
root.title('Pancake Gcode Generator')
root.resizable(False, False)
root.geometry('350x500')
varColor = tk.IntVar()

pancakesImg = PhotoImage(file="tkImg\pancakes.png")
grillImg = PhotoImage(file="tkImg\grill.png")

myFont = font.Font(family='Helvetica')

label = Label(
    root,
    image=pancakesImg
)
label.place(x=0, y=0)

def select_file():
    filetypes = (('text files', '*.jpg'),)

    filename = fd.askopenfilename(
        title='Open a .jpg',
        initialdir='/',
        filetypes=filetypes)
    makeInstuctions.makeInstuctions(filename, 152.4, 152.4, colorButtonVar.get(), edgButtonVar.get())


# open button
open_button = tk.Button(
    root,
    text='Open a File',
    image = grillImg,
    compound = CENTER,
    font = myFont,
    fg = 'White',
    width=100,
    height=200,
    bg='white',
    command=select_file
)

#the color picker
colorButtonVar = tk.IntVar()
colorButtonVar.set(0)  # initializing the choice, i.e. Python

colors = [("Black", 0), ("White", 255), ("Gray", 127)]

def ShowChoice():
    print(colorButtonVar.get())

for colors, val in colors:
    tk.Radiobutton(root, 
                   text=colors,
                   padx = 20, 
                   variable=colorButtonVar, 
                   command=ShowChoice,
                   value=val).grid(row = val + 2,sticky='W')

#lable
lable = tk.Label(root, text="Gavin's Great G-Code Generator!", font='Times 18')

#check box
edgButtonVar = tk.IntVar()

tk.Checkbutton(root, text="Edge File", variable=edgButtonVar, onvalue = True, offvalue = False).grid(row = 2, sticky='E', padx = 20)

open_button.grid(column=0, row=1, padx=10, pady=20)
lable.grid(column=0, row=0, padx=10, pady=15)

# run the application
root.mainloop()