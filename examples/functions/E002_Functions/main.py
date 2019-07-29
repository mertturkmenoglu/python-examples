# Example 018: Function Arguments


# Default arguments
# This type of arguments must come after
# non-default type arguments
def print_message(name, message='Hi'):
    """Prints the given message and the name"""
    print(message + " " + name)


def add_numbers(*numbers):
    """Adds numbers and then returns the sum"""
    sum_of_numbers = 0

    for number in numbers:
        sum_of_numbers += number

    return sum_of_numbers


# Message will be default value
print_message("John")

# Message will be "Good morning"
print_message("Emily", "Good morning")

# Keyword arguments
print_message(message="Good night", name="Clark")

# Variadic function
result = add_numbers(3, 4, 5)
print(result)

result = add_numbers(3, 4, 5, 6)
print(result)
