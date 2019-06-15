# Example 019: Recursion example

def findFactorial(num):
    """Find the factorial of the given number"""
    if num == 1:
        return 1
    else:
        return num * findFactorial(num - 1)

x = 4
print(findFactorial(x))

x = 5 
print(findFactorial(x))
