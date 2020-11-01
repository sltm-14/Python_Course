# path = "/Users/sltm1/Documents/REPASO/Python/Python_Basics/4.-Scripting/recortes"
#
# path = path[::-1]
#
# index = path.find('/')
#
# path = path[index:]
#
# path = path[::-1]
#
# print(path)




# for c in string[::-1]:
#     if (c == '/'):
#         print("Found")
#
# name='Carem'

string = "/Users/sltm1/Documents/REPASO/Python/Python_Basics/4.-Scripting/recortes"
for count,ele in enumerate(string[::-1]):
        if (ele == '/'):
            string = string[:-count]
            break

print(string)


# for count,ele in enumerate(string[::-1]):
#     if (ele == '/'):
#
#         string = string[:count]
#         break
#
# print(string)
