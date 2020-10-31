import os
import tkinter # only import tkinr

def inputText():
    path = textBox.get()
    etiqueta["text"] = path

window = tkinter.Tk()
window.geometry("500x300")

textBox = tkinter.Entry(window,font = "Helvetica 20") #window en la que se muestra, fuente tamaño de letra
textBox.pack()

boton = tkinter.Button(window,text = "click",command = inputText)
boton.pack()

window.mainloop()


path = "/Users/sltm1/Documents/REPASO/Python/Python_Basics/4.-Scripting/recortes"
try:
    os.mkdir(path)
except OSEError:
    print("Creation of directory %s failsed" % path)
else:
    print("Directory succesfully created %s" % path)
