# Lambda expressions test


def return_quadratic_function(a, b, c):
    """ This function returns a function f(x) = a^2*x + b*x + c """
    return lambda x: a * (x ** 2) + b * x + c


# Driver code
f = return_quadratic_function(1, -2, 1)
print(f(1))

print(return_quadratic_function(1, -4, 4)(4))
