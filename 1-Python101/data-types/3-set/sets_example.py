""" - EMPTY LIST ------------------------------------------------------------- """

empty_set = set()

""" Everytime you run the code the items in the set will appear in different order """
names = {"Mateo","Andrea","Ximena","Nicolas"}
print(names)

""" If you repeat an item more than once it will not be considered """

names = {"Mateo","Andrea","Ximena","Nicolas","Ximena"}
print(names)

""" - GET THE INDEX OF AN ELEMENT FROM LIST --------------------------------------------------- """

names = {"Mateo","Andrea","Ximena","Nicolas","Ximena"}
print('Nicolas' in names)

""" - SHOW THE ITEMS THAT TWO SETS HAVE IN COMMON AND THE ONES THAT THEY DON'T ---------------- """

names_01 = {"Carla","Andrea","Andrew","Nicolas"}
names_02 = {"Mateo","Andrea","Ximena","Nicolas"}

print(names_01.intersection(names_02))
print(names_01.difference(names_02))

""" - ADD THE ITEMS OF TWO SETS IN ONE -------------------------------------------------------- """

names = names_01.union(names_02)
print(names)
