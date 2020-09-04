# try:
#     Code to be executed
# except:
#     Code to run to handle sxceptions
#Finally:
#     Set of statements
#     Examples: Close file, release sources

try:
    print("Enter a file name:")
    name = input()
    file = open(name,'w')

except:
    print("Error with file")
    print("Enter a file name")
    name = input()
    file = open(name,'w')

finally:
    file.close()
