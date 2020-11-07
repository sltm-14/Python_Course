# 1.- Put most code into into a function or class
# 2.- Use __name__ to control execution of code
# 3.- Create a function called main() to contain the code you want to run
# 4.- Call other functions from main()

from time import sleep

print("This is my file to demostrate best practices")

def process_data(data):
    print("Beginning data processing")
    modified_data = data + " that has been modified"
    sleep(3)
    print("Data processing finished")
    return modified_data

def read_data_from_web():
    print("Reading data from web")
    data = "Data from the web"
    return data

def write_data_to_database(data):
    print("Writing data to a database")
    print(data)

def main():
    data = read_data_from_web()
    modified_data = process_data(data)
    write_data_to_database(modified_data)

if __name__ == "__main__":
    main()
