class bluse:
    def __init__(self, size, color):
        self.size = size
        self.color = color

    def bluseInfo(self):
        print("Size: " + str(self.size) + " Color: " + self.color)

b1 = bluse(9,"Rot")
b2 = bluse (10,"Rosa")

class human:
    def __init__(self,name,age):
        self.name = name
        self.age = age

h1 = human("Anna", 17)
h2 = human("Sarah", 19)

h1.myBluse = b2

h1.myBluse.bluseInfo()
