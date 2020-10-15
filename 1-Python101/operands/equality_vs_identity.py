# "==" checks for equiality
# "is" checks for identity ( used when we want to check if it's the same object in memory)

l1 = [1,2,3,4,5]
l2 = [1,2,3,4]

if l1 == l2:
    print(True)
else:
    print(False)

# Answer: False

l1 = [1,2,3,4,5]
l2 = [1,2,3,4,5]

if l1 == l2:
    print(True)
else:
    print(False)

# Answer: True

l1 = [1,2,3,4,5]
l2 = [1,2,3,4,5]

if l1 is l2:
    print(True)
else:
    print(False)

# Answer: False

l1 = [1,2,3,4,5]
l2 = l1 # If we change une of those lists it will also change the other

if l1 is l2:
    print(True)
else:
    print(False)

# Answer: True
