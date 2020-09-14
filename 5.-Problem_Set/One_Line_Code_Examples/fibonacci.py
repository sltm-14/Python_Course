
fib = lambda x: x if x <= 1 else fib(x - 1) + (x - 2)

print(fib(5))
