def fibonacci(n):
    if(0 == n):
        res = 0
    elif(1 == n):
        res = 1
    else:
        res = fibonacci(n-1) + fibonacci(n-2)

    return res

fib_arr[] =

def fibonacci_dynamic(n):
    if(0 == n):
        res = 0
    elif(1 == n):
        res = 1
    else:
        res = fibonacci(n-1) + fibonacci(n-2)

    return res

print(fibonacci(8))
