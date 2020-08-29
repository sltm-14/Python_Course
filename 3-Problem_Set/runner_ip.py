n = int(input("Number of participants: "))
scores = map(int, input("Scores: ").split())

print(scores)

scores.remove(max(scores))

print(scores)
