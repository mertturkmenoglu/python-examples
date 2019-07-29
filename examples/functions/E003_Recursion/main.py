# Example 019: Recursion example


def find_factorial(num):
    """Find the factorial of the given number"""
    if num == 1:
        return 1
    else:
        return num * find_factorial(num - 1)


x = 4
print(find_factorial(x))

x = 5 
print(find_factorial(x))
