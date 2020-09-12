from PIL import Image
import os

def crop_image(origin_route,destination_route,x1,y1,x2,y2):
    contenido = os.listdir(origin_route)

    for picture in (contenido):
        dir = origin_route + "/" + picture
        im = Image.open(dir)
        cropped = im.crop((x1,y1,x2,y2))
        dir = destination_route + picture
        cropped = cropped.save(dir)
        print(picture)


origin_path_up      = '/Users/sltm1/Documents/REPASO/Python/4.-Scripting/crop_images/Capturas_aleman_origin/up'
destination_path_up = '/Users/sltm1/Documents/REPASO/Python/4.-Scripting/crop_images/Capturas_aleman/'

x1_up = 0
y1_up = 0
x2_up = 1920
y2_up = 1076


origin_path_down      = '/Users/sltm1/Documents/REPASO/Python/4.-Scripting/crop_images/Capturas_aleman_origin/Down'
destination_path_down = '/Users/sltm1/Documents/REPASO/Python/4.-Scripting/crop_images/Capturas_aleman/'

x1_down = 230
y1_down = 1080
x2_down = 1594
y2_down = 1840


origin_path_left      = '/Users/sltm1/Documents/REPASO/Python/4.-Scripting/crop_images/Capturas_aleman_origin/Left'
destination_path_left = '/Users/sltm1/Documents/REPASO/Python/4.-Scripting/crop_images/Capturas_aleman/'

x1_left = 0
y1_left = 0
x2_left = 1920
y2_left = 1080

origin_path_right      = '/Users/sltm1/Documents/REPASO/Python/4.-Scripting/crop_images/Capturas_aleman_origin/Right'
destination_path_right = '/Users/sltm1/Documents/REPASO/Python/4.-Scripting/crop_images/Capturas_aleman/'

x1_right = 1370
y1_right = 0
x2_right = 3286
y2_right = 1080


crop_image(origin_path_up,    destination_path_up,    x1_up,    y1_up,    x2_up,    y2_up)
crop_image(origin_path_down,  destination_path_down,  x1_down,  y1_down,  x2_down,  y2_down)
crop_image(origin_path_left,  destination_path_left,  x1_left,  y1_left,  x2_left,  y2_left)
crop_image(origin_path_right, destination_path_right, x1_right, y1_right, x2_right, y2_right)
