a = [1,3,5,7,2,2,4,6,8,1,2,3,4,5,6,7,8,9,1,3,7,5,5,5,5,5]
print(a)
most = max(set(a), key=a.count)
print(most)

most = max(a)
print(most)
