# Example 026: Strings
import math

# Create a string
message = 'Hi John'
print(message)

# Accessing via index
word = "kadikoy"
for i in range(len(word)):
    print('{} th letter is: {}'.format(i, word[i]))

# Negative indexing
word = "Madam I'm Adam"
print('Normal: ', word)
for i in reversed(range(len(word))):
    print('{} - th letter is: {}'.format(i, word[i]))

# Concatenation
first = "War"
second = "and"
third = "Peace"

name = first + ' ' + second + ' ' + third
print('Book: ', name)

# Repetition
message = 'Ni!' * 3
print(message)

# Iteration
word = "kadikoy"
for letter in word:
    print(letter)

# enumerate()
enumeration = list(enumerate(word))
print('list(enumerate({}): {}'.format(word, enumeration))

# String length
print('Word: {} Length: {}'.format(word, len(word)))


# Formatting

# Number base
print("Decimal: {0}\tBinary: {0:b}".format(15))

# Scientific notation
print("Normal: {0}\tScientific: {0:e}".format(math.pi))

# Rounding
print("Normal: {0}\t4 digit after full stop: {0:.3f}".format(math.pi))

# Alignment
print("|{:<8}|{:^8}|{:>8}|".format('ID', 'Name', 'Surname'))

# To lower case
print('Normal: {}\tLower case: {}'.format("sPoNgE bOB", "sPoNgE bOB".lower()))

# To upper case
print('Normal: {}\tUpper case: {}'.format("sPoNgE bOB", "sPoNgE bOB".upper()))

# Split string into tokens
print('This is a sentence and it will be split to tokens'.split())

# Join strings
print(' '.join(['Mazhar', 'Fuat', 'Ozkan', '-', 'Ali', 'Desidero']))

# Find substring
print("This is a string".find('st'))

# Replace a substring
print('You are the knight who say "Ni!"'.replace('You', 'We'))