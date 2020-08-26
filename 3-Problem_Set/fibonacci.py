def fibonacci(n):
    if (n == 1 or n == 2):
        result = 1
    else:
        result = fibonacci(n-1) + fibonacci(n-2)

    return result


print(fibonacci(100))
