
def main():
    print ("{}".format(__name__))

# Is this file being run directly by python? or is it being imported?
if __name__ == '__main__':
    print("Run directly")
    main() # Output: __main__
else:
    print("Run from Import")
    main() # Output: main_module
