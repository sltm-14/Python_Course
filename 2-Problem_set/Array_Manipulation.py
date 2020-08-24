n = 5
m = 3
queries = [[1, 2, 100], [2, 5, 100], [3, 4, 100]]
n = 5

listIntegration = []

"""
for i in range (n):
    listIntegration.append(0)

print(queries[0][2])

for y in range (len(queries)):
    for x in range (queries[y][0]-1,queries[y][1]):
        listIntegration[x] = listIntegration[x] + queries[y][2]

"""

n, m = map(int,input().split())
a = [0] * (n+1)

print("N: " + str(n) + " M: " + str(m) )
print( a )

for _ in range(m):
    f, l, val = [int(n) for n in input().split()]
    a[f-l]+=val
    if ( l <= n):
        a[l]-=val
    print(a)


print(max(a))
