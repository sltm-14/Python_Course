queries = [[1, 2, 100], [2, 5, 100], [3, 4, 100]]
n = 5

listIntegration = []

for i in range (n):
    listIntegration.append(0)

print(queries[0][2])

for y in range (len(queries)):
    for x in range (queries[y][0]-1,queries[y][1]):
        listIntegration[x] = listIntegration[x] + queries[y][2]


print(listIntegration)
print(max(listIntegration))
