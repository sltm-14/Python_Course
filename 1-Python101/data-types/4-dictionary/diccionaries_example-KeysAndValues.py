new_diccionary = {}
print(new_diccionary)

student = {'Name': 'John', 'Age': 25, 'Courses': ['Math, History']}
people = {1:'Anna', 2:'Francisco',3:'Jorge'}


print(student['Courses'])
print(student.get('Name', 'Not found'))

print(people[3])

student['phone'] = '111-1111'

print(student)

student['Age'] = 24
print(student)

student.update({'phone':'222-2222'})
print(student)

age = student.pop('Age')
print(student)
print(age)


print(len(student))

print(student.keys())
print("KEYSSSSSSS")
diccKeys = []
diccKeys = list(student.keys())
print(diccKeys)
diccKeys.reverse()
print(diccKeys)
print(student.values())
print(student.items())

for key in student:
    print(key)

print("Key and value")

for key, value in student.items():
    print(key,value)

my_map = {'a': 1, 'b': 2}
inv_map = {v: k for k, v in my_map.items()}
