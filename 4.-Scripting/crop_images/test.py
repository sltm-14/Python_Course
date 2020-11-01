import os
from PIL import Image
import tkinter as tk


window = tk.Tk()
window.geometry("500x300")
v = tk.IntVar()
v.set(1)  # initializing the choice, i.e. Python
pos = 0

cropingOptions = [
    ("Up",0),
    ("Down",1),
    ("Right",2),
    ("Left",3)
]

#            up    down  left  right
x1_list = [   0,  230,    0, 1370]
y1_list = [   0, 1080,    0,    0]
x2_list = [1920, 1594, 1920, 3286]
y2_list = [1076, 1840, 1080, 1080]

def getInputText():
    origin_path = textBox.get()
    origin_path = input("Insert Origin path: ")
    origin_path = origin_path.replace[2:]
    origin_path = origin_path.replace('\\','/')
    return origin_path

def crop_image(x1_,y1_,x2_,y2_):
    path = getInputText()
    contenido = os.listdir(path)

    for picture in (contenido):
        dir = path + "/" + picture
        im = Image.open(dir)
        cropped = im.crop((x1_,y1_,x2_,y2_))
        dir = path + picture
        cropped = cropped.sa

def ShowChoice():
    pos = v.get()


textBox = tk.Entry(window,font = "Helvetica 18") #window en la que se muestra, fuente tamaño de letra
textBox.pack()

etiqueta = tk.Label(window)
etiqueta.pack()

boton = tk.Button(window,text = "click",command = crop_image(x1_list[pos],y1_list[pos],x2_list[pos],y2_list[pos]))
boton.pack()

# tk.Label(window,
#          text="""Enter the path of the FOLDER with the images and select a possition to crop:""",
#          justify = tk.LEFT,
#          padx = 20).pack()
#
# for val, language in enumerate(cropingOptions):
#     tk.Radiobutton(window,
#                   text=language,
#                   padx = 20,
#                   variable=v,
#                   command=ShowChoice,
#                   value=val).pack(anchor=tk.W)

window.mainloop()


path = "/Users/sltm1/Documents/REPASO/Python/Python_Basics/4.-Scripting/recortes"

try:
    os.mkdir(path)
except OSEError:
    print("Creation of directory %s failed" % path)
else:
    print("Directory succesfully created %s" % path)
