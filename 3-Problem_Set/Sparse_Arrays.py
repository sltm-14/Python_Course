
strings  = ['abcde','sdaklfj','asdjf','na','basdn','sdaklfj','asdjf','na','asdjf','na','basdn','sdaklfj','asdjf']
queries = ['abcde','sdaklfj','asdjf','na','basdn']

print(strings)
print(queries)

slen = len(strings)
qlen = len(queries)

print(slen)
print(qlen)
res = []

rep = 0

for x in range (qlen):
    for y in range (slen):
        if (queries[x] == strings[y]):
            rep = rep + 1

    res.append(rep)
    rep = 0

print(res)
