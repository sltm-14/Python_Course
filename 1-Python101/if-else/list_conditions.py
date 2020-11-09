subs   = 2400
likes  = 2000
comments = 75

conditions = [
    subs     > 150,
    likes    > 150,
    comments >  50
]

if all(conditions):
    print("All conditions are fullfiled")
