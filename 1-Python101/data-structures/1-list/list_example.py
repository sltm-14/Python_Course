
my_list = [1, 2, "Anna", 'N', 9, 7.1]
print(my_list)

#Output: [1, 2, 'Anna', 'N', 9, 7.1]

""" - ADD ELEMENTS TO LIST -------------------------------------------------------- """

my_list.append(3)
print(my_list)

#Output: [1, 2, 'Anna', 'N', 9, 7.1, 3]

my_list.append([4, 1])
print(my_list)

#Output: [1, 2, 'Anna', 'N', 9, 7.1, 3, [4, 1]]

my_list.extend([4, 1])
print(my_list)

#Output: [1, 2, 'Anna', 'N', 9, 7.1, 3, [4, 1], 4, 1]

my_list.insert(4, "insert() example")
print(my_list)

# Output: 1, 2, 'Anna', 'N', 'insert() example', 9, 7.1, 3, [4, 1], 4, 1]

print(my_list[-1])
# Output: 1
print(my_list[-3])
# Output: [4, 1]
print(my_list[-9])
# Output: Anna

""" - DELETE ELEMENTS FROM LIST --------------------------------------------------- """
