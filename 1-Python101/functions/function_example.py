

# Function that returns the addition of two numbers
def increment_example_1(number, by):
    return number + by


x = increment_example_1(2, 3)

print(x)


# Function that returns the original value and the addition, it is received as a tuple
def increment_example_2(number, by):
    return (number, number + by)


x = increment_example_2(2, 3)

print(x)


# Function that returns the original value and the addition, it is received as two different values
def increment_example_3(number, by):
    return (number, number + by)


x, y = increment_example_3(2, 3)

print(x, y)


# Function that returns the original value and the addition, it is received as a list
def increment_example_4(number, by):
    return [number, number + by]


x = increment_example_4(2, 3)

print(x)


# By adding keyword arguments, the code is more readable
def increment_example_5(number, by):
    return [number, number + by]


x = increment_example_5(number=2, by=3)

print(x)


# Parameters can have a predefined value in case the user does not specify
def increment_example_6(number, by=5):
    return [number, number + by]


x = increment_example_6(number=4)

print(x)


# The type of value of the expected parameters or the returning value can be specified
def increment_example_7(number: int, by: int = 4) -> int:
    return number + by


x = increment_example_7(number=7)

print(x)
