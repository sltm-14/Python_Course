from PIL import Image
import os

def crop_image(origin_route,destination_route,x1_,y1_,x2_,y2_):
    contenido = os.listdir(origin_route)

    for picture in (contenido):
        dir = origin_route + "/" + picture
        im = Image.open(dir)
        cropped = im.crop((x1_,y1_,x2_,y2_))
        dir = destination_route + picture
        cropped = cropped.save(dir)
        print(picture)

#     up    down  left  right
x1_list = [   0,  230,    0, 1370]
y1_list = [   0, 1080,    0,    0]
x2_list = [1920, 1594, 1920, 3286]
y2_list = [1076, 1840, 1080, 1080]

origin_path = input("Insert Origin path: ")
origin_path = origin_path.replace("C:","")
origin_path = origin_path.replace('\\','/')

destination_path = input("Insert destination path: ")
destination_path = destination_path.replace("C:","")
destination_path = destination_path.replace('\\','/')
destination_path = destination_path + '/'

position = int(input("Position of the screen to keep:\n0.-Up\n1.-Down\n2.-Left\n3.-Right\n\n"))

if(0 <= position < 4):
    x_1 = x1_list[position]
    y_1 = y1_list[position]
    x_2 = x2_list[position]
    y_2 = y2_list[position]
    print(origin_path)
    print(destination_path)
    crop_image( origin_path, destination_path, x_1, y_1, x_2, y_2 )
else:
    print("Not a valid option")
