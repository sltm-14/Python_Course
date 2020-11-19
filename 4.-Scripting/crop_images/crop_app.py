import os
from PIL import Image
import tkinter as tk

window = tk.Tk()
window.geometry("500x300")

rb = tk.IntVar()
rb.set(0)  # initializing the choice, i.e. Python
opt = 0
y_pos = 60

cropingOptions = [
    ("Up",0),
    ("Down",1),
    ("Left",2),
    ("Right",3)
]

#     up    down  left  right
x1 = [   0,  230,    0, 1920]
y1 = [   0, 1080,    0,    0]
x2 = [1920, 1594, 1920, 3840]
y2 = [1080, 1840, 1080, 1080]

def getPosotionToCrop():
    opt = rb.get()
    print(opt)

def createNewFolder(path):
    try:
        os.mkdir(path)
    except OSEError:
        print("Creation of directory %s failed" % path)
    else:
        print("Directory succesfully created %s" % path)

def crop_image():

    opt = rb.get()
    print(x1[opt],y1[opt],x2[opt],y2[opt])

    origin_path = tb_path.get()
    origin_path = origin_path[2:]
    origin_path = origin_path.replace('\\','/')

    destination_path = origin_path + "_recortes/"
    createNewFolder(destination_path)

    contenido = os.listdir(origin_path)

    for picture in (contenido):
        dir = origin_path + "/" + picture
        im = Image.open(dir)

        cropped = im.crop((x1[opt],y1[opt],x2[opt],y2[opt]))

        dir = destination_path + picture
        cropped = cropped.save(dir)

        print(picture)

    tk.Label(window,
             text="""FINISHED        """,
             justify = tk.LEFT,
             padx = 20).place(x=200, y=250)


tb_path = tk.Entry(window, font = "Helvetica 12")
tb_path.place(x=50, y=30, height = 25, width = 400)

for val, cropingOption in enumerate(cropingOptions):
    y_pos = y_pos + 25
    tk.Radiobutton(window,text=cropingOption, padx = 20, variable=rb, command=getPosotionToCrop,
                   value=val).place(x = 200, y = y_pos)

bt_Crop = tk.Button(window, text = "Crop", command = crop_image)
bt_Crop.place(x=210, y=200, height = 25, width = 80)


window.mainloop()
