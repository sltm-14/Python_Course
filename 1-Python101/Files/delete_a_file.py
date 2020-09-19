import os

if(os.path.exists(r"C:\Users\sltm1\Documents\REPASO\Python\1-Python101\Files\example.txt")):
    os.remove(r"C:\Users\sltm1\Documents\REPASO\Python\1-Python101\Files\example.txt")
    print("File deleted.")
else:
    print("File not found.")
