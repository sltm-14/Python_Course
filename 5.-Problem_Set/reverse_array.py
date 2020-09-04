def reverseArray(a):
    res = []

    for x in range(len(a)-1,-1,-1):
        res.append(a[x])

    return res


numbers = [9, 8, 4, 7, 4, 3, 1, 6, 5]
result = reverseArray(numbers)

print(result)
