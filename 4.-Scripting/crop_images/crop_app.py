import os
from PIL import Image
import tkinter as tk


def getInputText():
    text = textBox.get()


window = tk.Tk()
window.geometry("500x300")

rb = tk.IntVar()
rb.set(1)  # initializing the choice, i.e. Python
pos = 0

cropingOptions = [
    ("Up",0),
    ("Down",1),
    ("Right",2),
    ("Left",3)
]

#            up    down  left  right
x1 = [   0,  230,    0, 1370]
y1 = [   0, 1080,    0,    0]
x2 = [1920, 1594, 1920, 3286]
y2 = [1076, 1840, 1080, 1080]

tb_path = tk.Entry(window,font = "Helvetica 20")
tb_path.grid(row = 4, column = 2)

bt_getPath = tk.Button(window,text = "click", command = getInputText)




window.mainloop()
