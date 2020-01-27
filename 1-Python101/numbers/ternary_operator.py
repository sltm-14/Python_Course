

age = 17

# TRADITIONAL

if 18 <= age < 65:
    print(str(age) + " is eligible\n")
else:
    print(str(age) + " is not eligible\n")

# TERNARY OPERATOR

message = "Eligible" if age >= 18 else "Not eligible"

print(message)
