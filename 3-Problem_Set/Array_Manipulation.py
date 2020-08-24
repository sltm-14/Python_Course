
queries = [[1, 2, 100], [2, 5, 100], [3, 4, 100]]
n = 5

listIntegration = [0] * n
"""
for y in range (len(queries)):
    for x in range (queries[y][0]-1,queries[y][1]):
        listIntegration[x] = listIntegration[x] + queries[y][2]
"""

for y in range (len(queries)):
    #listIntegration[queries[y][0]-1:queries[y][1]] = listIntegration[queries[y][0]-1:queries[y][1]] + [queries[y][2]]
    #listIntegration[queries[y][0]-1:queries[y][1]] = map(sum, zip(listIntegration[queries[y][0]-1:queries[y][1]], (((queries[y][1] - queries[y][0]) + 1) * [queries[y][2]]) ))



    listIntegration[queries[y][0]-1:queries[y][1]]  = tuple(map(lambda x: x[0] + x[1], zip( listIntegration[queries[y][0]-1:queries[y][1]] , (((queries[y][1] - queries[y][0]) + 1) * [queries[y][2]]) )))

print(listIntegration)
print ("aaaaaaaaaaaaah")
print(max(listIntegration))

"""print ("----------------------------------------------")


first = [1, 2, 3, 4, 5]
second = [6, 7, 8, 9, 10]

third  = tuple(zip(first,second))
print(third)

third  = tuple(map(lambda x: x[0] + x[1], zip(first, second)))

print(first)
print(second)
print(tuple(third))
"""
