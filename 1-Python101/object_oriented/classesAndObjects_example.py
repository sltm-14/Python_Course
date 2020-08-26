class bluse:
    def __init__(self, size, color):
        self.size = size
        self.color = color

    def bluseInfo(self):
        print("Size: " + str(self.size) + " Color: " + self.color)


b1 = bluse(9,"Rojo")
b1.bluseInfo()
