# Set attribute
# Get attribute

class Person():
    pass

person = Person()

first_key = 'first'
first_val = 'Corey'

setattr(person,first_key,first_val)

first = getattr(person,first_key)

print(first)
print(person.first)

print("\n")

person_info = {'first':'Corey','last':'Schafer'}

for key,value in person_info.items():
    setattr(person,key,value)

print(person.first)
print(person.last)

print("\n")

for key in person_info.keys():
    print(getattr(person,key))
