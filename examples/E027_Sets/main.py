# Example 027: Set example

# Unordered collection
# Unique items
# Items must be immutable
# A set is mutable
# We can add or remove item



# ------------------------------------- #
# Create empty set
empty_set = set()
print(type(empty_set))
# ------------------------------------- #

print('\n' * 3)

# ------------------------------------- #
# Define a basic set
number_set = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
print(number_set)
# ------------------------------------- #

print('\n' * 3)

# ------------------------------------- #
# Mixed set
mixed_set = {"Doctor Who", 10, (0, 2, 4, 6, 8)}
print(mixed_set)
# ------------------------------------- #

print('\n' * 3)

# ------------------------------------- #
# Set with duplicate elements
# They will be discarded.
duplicate = {0, 0, 0, 1, 1, 2, 3, 4, 5}
print(duplicate)
# ------------------------------------- #

print('\n' * 3)

# ------------------------------------- #
# Set can not contain mutable objects
# set cannot have mutable items
even = set([0, 2, 4, 6, 8])
print(even)
# ------------------------------------- #

print('\n' * 3)

# ------------------------------------- #
# Add an element
odd_set = {1, 3}
print('Odd numbers: ', odd_set)
odd_set.add(5)
print('Odd numbers: ', odd_set)
odd_set.update([7, 9])
print('Odd numbers: ', odd_set)
# ------------------------------------- #

print('\n' * 3)

# ------------------------------------- #
# initialize my_set
number_set = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
print('At first:', number_set)

number_set.discard(4)
print('Discard 4: ', number_set)

number_set.remove(6)
print('Remove 6: ', number_set)

number_set.discard(2)
print('Discard 2: ', number_set)
# ------------------------------------- #

print('\n' * 3)

# ------------------------------------- #
# Methods
word = set("kadikoyistanbul")
print('Word: ', word)

# Pop
word.pop()
print('Word: ', word)

word.pop()
print('Word:', word)

# Clear
word.clear()
print(word)
# ------------------------------------- #

print('\n' * 3)

# ------------------------------------- #
# Init sets
first = {1, 2, 3, 4, 5}
second = {4, 5, 6, 7, 8}

print('First set: ', first)
print('Second set: ', second)

# Operators
print('Using operators')
print('first | second: {}'.format(first | second))
print('second | first: {}'.format(second | first))

print('first & second: {}'.format(first & second))
print('second & first: {}'.format(second & first))

print('first - second: {}'.format(first - second))
print('second - first: {}'.format(second - first))

print('first ^ second: {}'.format(first ^ second))
print('second ^ first: {}'.format(second ^ first))

#Functions
print('Using functions')
print('first.union(second): {}'.format(first.union(second)))
print('second.union(first): {}'.format(second.union(first)))

print('first.intersection(second): {}'.format(first.intersection(second)))
print('second.intersection(first): {}'.format(second.intersection(first)))

print('first.difference(second): {}'.format(first.difference(second)))
print('second.difference(first): {}'.format(second.difference(first)))

print('first.symmetric_difference(second): {}'.format(first.symmetric_difference(second)))
print('second.symmetric_difference(first): {}'.format(second.symmetric_difference(first)))
# ------------------------------------- #

print('\n' * 3)

# ------------------------------------- #
# in / not in
word = set("kadikoy")
print('Word: ', word)
print("'a' in word: ", 'a' in word)
print("'p' not in word: ", 'p' not in word)
# ------------------------------------- #

print('\n' * 3)

# ------------------------------------- #
# Iteration
for letter in set("kadikoy istanbul"):
    print(letter)
# ------------------------------------- #

print('\n' * 3)

# ------------------------------------- #
# Frozenset
first  = frozenset([1, 2, 3, 4, 5])
second = frozenset([3, 4, 5, 6, 7])

print('first.isdisjoint(second): ', first.isdisjoint(second))
print('first.difference(second): ', first.difference(second))
print('first | second: ', first | second)