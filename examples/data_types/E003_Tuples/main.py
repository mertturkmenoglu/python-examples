# Example 025: Tuples

# Create empty tuple
empty_tuple = ()
print('Empty Tuple: ', empty_tuple)

number_tuple = (1, 2, 3)
print('Another Tuple: ', number_tuple)

mixed_tuple = (42, "Answer", 2.78)
print('Mixed Tuple: ', mixed_tuple)

nested_tuple = ("Keanu", ["Neo", 1, 33], (1, 2, 3))
print('Nested Tuple: ', nested_tuple)

# Declaring without parenthesis
new_tuple = 3, 4.6, "dog"
print(new_tuple)

# Tuple unpacking
integer, floating, string = new_tuple

print(integer)
print(floating)
print(string)

# Creating a tuple with one element
numbers = (1,)
print(type(numbers))

# Indexing
word = ('k', 'a', 'd', 'i', 'k', 'o', 'y')

print(word[0])
print(word[1])
print(word[2])
print(word[3])
print(word[4])
print(word[5])
print(word[6])

# Nested Tuple Indexing
print(nested_tuple[1][2])
print(nested_tuple[2][1])

# Negative Indexing
word = ('k', 'a', 'd', 'i', 'k', 'o', 'y')
print(word[-1])
print(word[-4])

# Slicing
word = ('k', 'a', 'd', 'i', 'k', 'o', 'y')
print(word[1:4])
print(word[:-7])
print(word[7:])
print(word[:])

# Mutable elements can be changed
special_tuple = ("Keanu", ["Neo", 1, 33], (1, 2, 3))
print(special_tuple)
special_tuple[1][0] = 9
print(special_tuple)

# Tuples can be reassigned
special_tuple = ('k', 'a', 'd', 'i', 'k', 'o', 'y')
print(special_tuple)

# Concatenation
print(("Witcher", "3", "CD") + ("Projekt", "Red"))

# Repetition
print(('Ni',) * 3)

# Methods
word = ('k', 'a', 'd', 'i', 'k', 'o', 'y')

print(word.count('p'))
print(word.index('o'))

# in / not in
word = ('k', 'a', 'd', 'i', 'k', 'o', 'y')

print('a' in word)
print('z' in word)
print('z' not in word)

for letter in word:
    print(letter)
