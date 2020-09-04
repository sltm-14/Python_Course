# try:
#     Code to be executed
# except:
#     Code to run to handle sxceptions

try:
    print("Enter a numerator")
    numer = int(input())
    print("Enter a denominator")
    denom = int(input())
    quotient = numer / denom
    print(quotient)
except :
#except ZeroDivisionError: #OnlyHandles the specified exceptions
    print("Cannot divide by zero")
    print("Enter a new denominator")
    denom = int(input())
    quotient = numer / denom
    print(quotient)
