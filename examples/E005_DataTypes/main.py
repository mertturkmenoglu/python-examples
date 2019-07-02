# Example 005: Data types example

# Python supports different data types:
# Integer
# String (you may know them as char arrays)
# Boolean (true or false)
# Python2 supports long but after python3, integer and long are merged
# Complex number from high school math(or university)
answer = 42
message = 'Ni!'
pi = 3.14
is_european_swallow = True
very_big_number = 1000
complex_number = 1 + 1j

# Lists. They are like arrays in other languages. 
# But they can contain multiple type items
# They are like dynamic containers
# We represent them within '[' and ']' characters
knights = ['Robin', 'Galahad', 'Lancelot', 'Sir Not Appearing In This Film']
hold_data = [answer, pi, knights, True]

# Tuples and lists are siblings. One big difference:
# List are mutable(they can be changed) but tuples are
# immutable(they can not be changed)
my_tuple = ('Coconuts', 'Squirrel', 7, False)

# Dictionaries. They are containers that holds values with unique keys
my_dictionary = {
    'name': "King Arthur",
    'age': 42,
    'alive': True
}

# Lets print them and see how they behave
# Print all the values and containers
print(answer)
print(message)
print(pi)
print(is_european_swallow)
print(very_big_number)
print(complex_number)
print(knights)
print(hold_data)
print(my_tuple)
print(my_dictionary)

# type() returns type of the object.
# Let's see Pythonian way to represent data
print(type(answer))
print(type(message))
print(type(pi))
print(type(is_european_swallow))
print(type(very_big_number))
print(type(complex_number))
print(type(knights))
print(type(hold_data))
print(type(my_tuple))
print(type(my_dictionary))