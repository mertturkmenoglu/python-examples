# Example 018: Function Arguments

# Default arguments
# This type of arguments must come after
# non-default type arguments
def printMessage(name, message = 'Hi'):
    """Prints the given message and the name"""
    print(message + " " + name)

def addNumbers(*numbers):
    """Adds numbers and then returns the sum"""
    sum = 0

    for number in numbers:
        sum += number
    
    return sum

# Message will be default value
printMessage("John")

# Message will be "Good morning"
printMessage("Emily", "Good morning")

# Keyword arguments
printMessage(message = "Good night", name = "Clark")

# Variadic function
sum = addNumbers(3, 4, 5)
print(sum)

sum = addNumbers(3, 4, 5, 6)
print(sum)