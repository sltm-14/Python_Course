while(1):
    n = input("Ingresa un numero: ")
    n = int(n)

    even = True if (n % 2 == 0) else False

    if( n > 20 and n <= 100 and even ):
        print("Not Weird")
    elif( n >= 6 and n <= 20 and even ):
        print("Weird")
    elif( n >= 2 and n <= 4 and even ):
        print("Not Weird")
    elif( n >= 1 and n <= 100 and (not even) ):
        print("Weird")
