# Dynamic programming example
fib_numbers = {1: 1, 2: 1, 3: 2}


def fibonacci(n: int) -> int:
    if n not in fib_numbers:
        fib_numbers[n] = fibonacci(n - 1) + fibonacci(n - 2)
    return fib_numbers[n]


print(fibonacci(7))
print(fibonacci(5))
