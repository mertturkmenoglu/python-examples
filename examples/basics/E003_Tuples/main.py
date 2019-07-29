# Example 003: Tuples
# Tuples are immutable objects

# Print tuple documentation
print(tuple.__doc__)

print('\n\n\n')

# Create a tuple.
# Tuples are like list but you can not change them
# So, operations on tuples are way faster than lists
# If you are sure that your values would not change, then
# you should definitely use tuples
my_tuple = ('monty python', 42, 3.14, 'ni!')

# They can contain multiple types
# For example, here, this tuple contains a string object and an
# integer object
another_tuple = ('king arthur', 3)

# Print tuples
print(my_tuple)
print(another_tuple)

# Another writing style
# Slicing
print(my_tuple[2:])

# Accessing via index
print(my_tuple[0])

# Appending tuples
my_tuple = my_tuple + another_tuple
print(my_tuple)
