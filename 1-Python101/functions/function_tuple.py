"""
To receive more than one parameter as a tuple, it is necesary 
to add * before the name of the parameter that will be received
"""


def multiply(*numbers):
    total = 1
    for x in numbers:
        total *= x

    return total


print(multiply(1, 2, 3, 4, 5))
