path = "/Users/sltm1/Documents/REPASO/Python/Python_Basics/4.-Scripting/recortes"

try:
    os.mkdir(path)
except OSEError:
    print("Creation of directory %s failed" % path)
else:
    print("Directory succesfully created %s" % path)
