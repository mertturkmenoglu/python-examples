# Example 008: Output formatting

# Create two dummy variable
x = 3
y = 4

# This is the Python3 way.
# You should use string format method.
print('Point: {} - {}'.format(x, y))

# You can specify variable name
print('x: {x}\ty: {y}'.format(x=x, y=y))

# Old, C style formatted output. Prefer not use to.
print('%d - %d' % (x, y))

# Take input
first = int(input('Enter the first integer: '))
second = int(input('Enter the second integer: '))

# Print formatted
print('You entered {} and {}'.format(first, second))
