# Example 003: Tuples
# Tuples are immutable objects

print(tuple.__doc__)

print('\n\n\n')

my_tuple = ('monty python', 42, 3.14, 'ni!')
another_tuple = ('king arthur', 3)

print(my_tuple)
print(another_tuple)

# Another writing style
print(my_tuple[2:])

# Accessing via index
print(my_tuple[0])

# Appending
my_tuple = my_tuple + another_tuple
print(my_tuple)
