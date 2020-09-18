new_File = open(r"C:\Users\sltm1\Documents\REPASO\Python\1-Python101\Files\example.txt","w")
new_File.write("Written from .py file")
new_File.close()

new_File = open(r"C:\Users\sltm1\Documents\REPASO\Python\1-Python101\Files\example.txt","r")
print(new_File.read())
