# How to raise your own exceptions

class rational:
    def __init__(self,x,y):
        numer = x
        if (y == 0):
            raise ZeroDivisionError()
        else:
            denom = y

try:
    rat1 = rational(4,1)
    print(rat1)
    rat2 = rational(3,0)
    print(rat2)
except:
    print("There was a problem")
