""" - EMPTY TUPLE ------------------------------------------------------------- """

empty_tuple = ()
empty_tuple = tuple()

""" Craete a tuple """
numbers = 1,2,3,4,5
print(type(numbers))

numbers = (1,2,3,4,5)
print(type(numbers))

""" The main difference between a list and a tupple is that you cannot modify a tuple, you just can acces to the values || READ ONLY"""

# Lists are mutuable
print("LISTS:\n")
names_1 = ["Mateo","Andrea","Ximena","Nicolas"]
names_2 = names_1

print(names_1)
print(names_2)

names_1[0] = 'Rhys'

print(names_1)
print(names_2)

# Tuples are not mutuable
print("\nTUPLES:\n")

names_1 = ("Mateo","Andrea","Ximena","Nicolas")
names_2 = names_1

print(names_1)
print(names_2)

# This would show an error message
# names_1[0]= 'Rhys'
#
# print(names_1)
# print(names_2)
