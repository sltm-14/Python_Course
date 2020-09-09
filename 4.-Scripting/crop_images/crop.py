import math

im = Image.open("example.jpg")
x1 = 0
y1 = 0
x2 = im.width
y2 = im.height
cropped = im.crop((x1,y1,x2,y2))
cropped.show()
