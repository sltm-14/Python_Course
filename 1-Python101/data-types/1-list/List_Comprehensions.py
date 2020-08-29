x = int(input("x: "))
y = int(input("y: "))
z = int(input("z: "))
n = int(input("n: "))

arr = [[X, Y, Z] for X in range(x+1) for Y in range(y+1) for Z in range(z+1)]

print(arr)

arr = [[X, Y, Z] for X in range(x+1) for Y in range(y+1) for Z in range(z+1) if X + Y + Z != n]
print("")
print(arr)
