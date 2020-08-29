""" - EMPTY LIST ------------------------------------------------------------- """

empty_list = []
empty_list = list()

""" - BASICS OF LISTS -------------------------------------------------------- """
my_list = [1, 2, "Anna", 'N', 9, 7.1]
print(my_list)

#Output: [1, 2, 'Anna', 'N', 9, 7.1]

print(my_list[-1])
# Output: 7.1
print(my_list[-3])
# Output: N
print(my_list[2:])
#Output: ['Anna', 'N', 9, 7.1]


""" - ADD ELEMENTS TO LIST -------------------------------------------------------- """

# append: adds whatever you put in the parenthesis to the end of the list

my_list.append(3)
print(my_list)

my_list.append("Hi")
print(my_list)

#Output: [1, 2, 'Anna', 'N', 9, 7.1, 3]

my_list.append([4, 1])
print(my_list)

#Output: [1, 2, 'Anna', 'N', 9, 7.1, 3, [4, 1]]

# Extends: adds, if you put a list in the parenthesis every velue is added as a different item at the end of the list

my_list.extend([4, 1])
print(my_list)

#Output: [1, 2, 'Anna', 'N', 9, 7.1, 3, [4, 1], 4, 1]

# Insert: adds what you put in the parenthesis in the position of the array that you indicate.

my_list.insert(4, "insert() example")
print(my_list)

# Output: 1, 2, 'Anna', 'N', 'insert() example', 9, 7.1, 3, [4, 1], 4, 1]

""" - DELETE ELEMENTS FROM LIST --------------------------------------------------- """
numbers = [1,2,3,4,5,1,2,3,4,5]

my_list.remove('N')
print(my_list)

numbers.remove(3)
print(numbers)

my_list.pop()
print(my_list)

popped = my_list.pop()
print(popped)

""" - REVERSE ELEMENTS FROM LIST --------------------------------------------------- """
numbers = [1, 2, 3, 4, 5]
print(numbers)

numbers.reverse()
print(numbers)

""" - SORT ELEMENTS FROM LIST --------------------------------------------------- """
numbers = [4,2,8,5,2,1,3]
print(numbers)

numbers.sort()
print(numbers)

numbers.sort(reverse=True)
print(numbers)

names = ["Mateo","Andrea","Ximena","Nicolas"]
print(names)

names.sort(reverse=True)
print(names)

names.sort()
print(names)

numbers = [4,2,8,5,2,1,3]
sorted_numbers = sorted(numbers)

print(numbers)
print(sorted_numbers)

# This would show an error
#
# my_list = [2, 1, "Anna", 'N', 9, 7.1]
# print(my_list)
#
# my_list.sort()
# print(my_list)

# To get the sorted version of the list without modifiying the original one we can use sorted()

print(max(numbers))
print(min(numbers))
print(sum(numbers))

""" - GET THE INDEX OF AN ELEMENT FROM LIST --------------------------------------------------- """
names = ["Mateo","Andrea","Ximena","Nicolas"]
print(names)

idx = names.index('Nicolas')
print(idx)

""" - INDEX OF ELEMENT IN THE LIST? --------------------------------------------------- """

names = ["Mateo","Andrea","Ximena","Nicolas"]
print('Jorge' in names)
print('Andrea' in names)

for index, name in enumerate(names):
    print(index,name)

""" - JOIN ELEMENTS IN THE LIST --------------------------------------------------- """

allNames = ' '.join(names)
print(allNames)

allNames = ' - '.join(names)
print(allNames)

""" - SPLIT ELEMENTS INTO LIST --------------------------------------------------- """

splitedNames = allNames.split(' - ')
print(splitedNames)

splitedNames = allNames.split(' ')
print(splitedNames)

splitedNames = allNames.split()
print(splitedNames)
