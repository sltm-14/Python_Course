""" Note: range takes a very small amount of memory, it is not a list, is a class of tipe range
    <class 'range'> """

# X takes the value of a character
for x in "Example 1  ":
    print(x)


# X takes the value of the object in the range
for x in ['Exmple', ' ', '2', '  ']:
    print(x)


# X tales a value from 0 to 5
for x in range(5):
    print(x)
print("\n")


# X tales a value from 4 to 9
for x in range(4, 9):
    print(x)
print("\n")


# X tales a value from 1 to 11 with steps of 2
for x in range(1, 11, 2):
    print(x)

new_list = [1, 11, 2]

for x in  new_list:
    print(x)

names = ["Mateo","Andrea","Ximena","Nicolas"]

for name in names:
    print(name)


def say_hello():
    print("Hello")

for i in range(5):
    print(i)
    say_hello()
