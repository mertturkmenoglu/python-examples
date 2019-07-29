# Example 028: Dictionary example

# Unordered collection
# Key - value pairs
# Retrieve Value via Key

# An item has a key and a value. They express a key-value pair
# Keys must be immutable and unique


# ------------------------------------------ #
# Create empty dictionary
empty_dict = {}
print('Empty dictionary: ', empty_dict)

# Dictionary with same type keys
movies = {1: 'Titanic', 2: 'Avatar'}
print('Movies: ', movies)

# Dictionary with mixed type keys
person = {
    'name': 'John',
    2: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
}
print('Person: ', person)

# Create dictionary using dict()
actors = dict({1: 'Keanu', 2: 'Leonardo'})
print('Actors: ', actors)
# ------------------------------------------ #

print('\n' * 3)

# ------------------------------------------ #
# Accessing elements
# To access values, you must use keys inside square brackets or with get() method
# get() returns None if the key is not found
# square brackets will return KeyError

jack = {
    "name": "Jack",
    "age": 18
}

print('jack["name"]: ', jack["name"])
print('jack.get("age"): ', jack.get("age"))
# ------------------------------------------ #

print('\n' * 3)

# ------------------------------------------ #
# Updating a dictionary

jack = {
    "name": "Jack",
    "age": 18
}

# Update
jack['age'] = 35
print('jack: ', jack)

# Add
jack['music'] = 'rock'
print('jack: ', jack)
# ------------------------------------------ #

print('\n' * 3)

# ------------------------------------------ #
# Removing
# pop(), pops and returns the value
# popitem(), pops and returns an arbitrary item
# clear(), clears all items
# del keyword may used

numbers = {
    0: 1,
    1: 2,
    2: 3,
    3: 4,
    4: 5
}

print('number.pop(4): ', numbers.pop(4))
print('numbers: ', numbers)

print('numbers.popitem(): ', numbers.popitem())
print('numbers: ', numbers)

del numbers[2]
print('numbers: ', numbers)

numbers.clear()
print('numbers: ', numbers)
# ------------------------------------------ #

print('\n' * 3)

# ------------------------------------------ #
# Creating dictionary from list

student_notes = {}.fromkeys(['John', 'Emily', 'Bruce'], 0)
print(student_notes)
# ------------------------------------------ #

print('\n' * 3)

# ------------------------------------------ #
# Getting items & keys
movies = {
    "Titanic": 1234,
    "Dark Knight": 854,
    "Arrival": 579
}

print('Movies: ', movies)

for item in movies.items():
    print(item)

print('Movies: ', movies)
list(sorted(movies.keys()))

print('Movies: ', movies)
# ------------------------------------------ #

print('\n' * 3)

# ------------------------------------------ #
# Dictionary comprehensions
odd_squares = {x: x * x for x in range(20) if x % 2 == 1}
print('odd_squares: ', odd_squares)

# in / not in
print(1 in odd_squares)
print(2 not in odd_squares)
print(49 in odd_squares)

# Iterating
for i in odd_squares:
    print(odd_squares[i])

# Methods
print(len(odd_squares))
print(sorted(odd_squares))
