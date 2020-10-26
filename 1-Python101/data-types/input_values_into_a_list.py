myList = input("Add all the values: \n")
myList = myList.replace(" ", "")
myList = myList.split('#')

print("\n\n")

print("Number of input values: " + str(len(myList)) )

myList =set(myList)
myList =list(sorted(myList))
print("Number of values in set: " + str(len(myList)) )

for tag in myList:
    print('#' + tag)

for tag in myList:
    print('#' + tag, end = ' ')
