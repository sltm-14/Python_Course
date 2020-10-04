
# You can loop as many lists as you want to using zip

names  = ["Anna", "Felipe", "Santiago", "Laura"]
genders = ["Woman", "Man","Man","Woman"]


for name, gender in zip(names,genders):
    print(f'{name} is a {gender}')
