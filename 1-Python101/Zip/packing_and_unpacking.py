# Paking in a tuple:
print("\n\nTUPLES:\n")
names  = ["Anna", "Felipe", "Santiago", "Laura"]
genders = ["Woman", "Man","Man","Woman"]


for value in zip(names,genders):
    print(value)

# Unpacking ______________________________________________________________________

print(f'\nLast value in tuple: {value}')
name_0, gender_0 = value

print(name_0, gender_0)

# if you only want to use one value use _

name, _ = value

print(name)

# Unpacing multiple values _______________________________________________________

n = (1,2,3,4,5,6,7,8,9)

a,b, *_,c, d = n

print(a,b,c,d)
