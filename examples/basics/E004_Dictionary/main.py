# Example 004: Dictionary
# Key : Value pairs
# Like hash-maps in Java

# Print dictionary documentation
print(dict.__doc__)
print('\n\n\n')

# Create a dictionary
# Whitespaces aren't necessary but i like them
# I think they helps understanding the structure
my_dictionary = {
    'name': 'king arthur', 
    'age': 42, 
    'color': 'blue'
}

# Print dictionary
print(my_dictionary)

# Print only keys
# We can access only keys
print(my_dictionary.keys())

# Print only values
# We can access only values
print(my_dictionary.values())
