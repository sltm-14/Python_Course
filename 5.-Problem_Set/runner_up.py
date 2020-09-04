#n = int(input("Number of participants: "))

scores = set(map(lambda x: int(x), input().split()))

scores.remove(max(scores))

print(max(scores))
