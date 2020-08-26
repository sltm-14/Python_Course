def fibonacci(n, memory):
    if memory[n] is not None:
        return memory[n]
    if n == 1 or n == 2:
        result = 1
    else:
        result = fibonacci(n-1, memory) + fibonacci(n-2, memory)
    memory[n] = result

    return result

def fib_memo(n):
    memory = [None] * (n + 1)
    return fibonacci(n, memory)


print(fib_memo(100))
