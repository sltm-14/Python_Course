def sum(*a):
    result = 0
    for i in a:
        result = result + i
    return result

res = sum(1,3,5,7,9,21,43,65,76,87,98)
print(res)
