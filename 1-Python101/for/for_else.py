
"""
    For/Else loops helps us not tu use flags in order to do something, 
    in this example if the foor loop finishes without "breaking" (entering to break)
    what's inside of else block will be executed
"""

names = ["Anna", "Michelle"]

for name in names:
    if name.startswith("K"):
        print("Found")
        break

else:
    print("Not found")
