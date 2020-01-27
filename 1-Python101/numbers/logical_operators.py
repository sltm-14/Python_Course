"""    FALSY VALUES:    0    ""    None    []   """


"""" NOT Operator ----------------------------------------------------------------------------------"""
# Empty string
name = ""

if not name:
    print("\nName is empty\n")
else:
    print(name)


# Not empty string
name = "Anna"

if not name:
    print("\nName is empty\n")
else:
    print(name)


# Blank space is not consudered True, but in python you should get rid of it
# so it can be fale
name = " "

if not name:
    print("\nName is empty\n")
else:
    print(name)

"""" AND Operator ----------------------------------------------------------------------------------"""

age = 22

if 18 <= age and age < 65:
    print(str(age) + " is eligible")
else:
    print(str(age) + " is not eligible")


# In python you can use:
#    18 <= age < 65    instead of    18 <= age and age < 65

age = 17

if 18 <= age < 65:
    print(str(age) + " is eligible")
else:
    print(str(age) + " is not eligible")
