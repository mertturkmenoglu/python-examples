# Example 023: Numbers

import decimal
import fractions
import math
import random


# ------------------------------------- #
# Integer
var = 1
print('Number: {}'.format(var))
print('Type: {}'.format(type(var)))
print('-' * 10)
# ------------------------------------- #

print('\n' * 3)

# ------------------------------------- #
# Float
var = 1.0
print('Number: {}'.format(var))
print('Type: {}'.format(type(var)))
print('-' * 10)
# ------------------------------------- #

print('\n' * 3)

# ------------------------------------- #
# Complex
var = 3 + 4j
print('Number: {}'.format(var))
print('Type: {}'.format(type(var)))
print('Is istance: {}'.format(isinstance(var, complex)))
print('-' * 10)
# ------------------------------------- #

print('\n' * 3)

# ------------------------------------- #
# Different base numbers
binary_number = 0b10101010
print('Binary number: {}'.format(binary_number))

hex_number = 0xA23
print('Hexadecimal number + 1: {}'.format(hex_number + 1))

oct_number = 0o32
print('Octal number: {}'.format(oct_number))
# ------------------------------------- #

print('\n' * 3)

# ------------------------------------- #
# Auto type conversion
first = 1
second = 2.0
result = first + second

print('Number: {}\tType: {}'.format(first, type(first)))
print('Number: {}\tType: {}'.format(second, type(second)))
print('Number: {}\tType: {}'.format(result, type(result)))
# ------------------------------------- #

print('\n' * 3)

# ------------------------------------- #
# Explicit Type Conversion
number = 2.3
print('Number: {}\tType: {}'.format(number, type(number)))
after = int(number)
print('Number: {}\tType: {}'.format(after, type(after)))

number = 1
print('Number: {}\tType: {}'.format(number, type(number)))
after = float(number)
print('Number: {}\tType: {}'.format(after, type(after)))
# ------------------------------------- #

print('\n' * 3)

# ------------------------------------- #
# Floating point error
first = 3.2
second = 1.1

print('first + second == 4.3\t:{}'.format(first + second == 4.3))
print('first + second = {}'.format(first + second))
# ------------------------------------- #

print('\n' * 3)

# ------------------------------------- #
# Decimal library examples
number = 3.14
print('Normal print: {}'.format(number))

print('With decimal.Decimal(): {}'.format(decimal.Decimal(number)))
result = decimal.Decimal('3.14') + decimal.Decimal('2.71')
print("decimal.Decimal('3.14') + decimal.Decimal('2.71') = {}".format(result))
# ------------------------------------- #

print('\n' * 3)

# ------------------------------------- #
# Fractions library examples
print('fractions.Fraction(3.14): {}'.format(fractions.Fraction(3.14)))
print('fractions.Fraction(10): {}'.format(fractions.Fraction(10)))
print('fractions.Fraction(2,5): {}'.format(fractions.Fraction(2,5)))
print('fractions.Fraction(1.1): {}'.format(fractions.Fraction(1.1)))
print("fractions.Fraction('1.1'): {}".format(fractions.Fraction('1.1')))
print('fractions.Fraction(2,5) + fractions.Fraction(2,5): {}'.format(fractions.Fraction(2,5) + fractions.Fraction(2,5)))
print('1 / fractions.Fraction(3,4): {}'.format(1 / fractions.Fraction(3,4)))
print('fractions.Fraction(-3,10) > 0: {}'.format(fractions.Fraction(-3,10) > 0))
# ------------------------------------- #

print('\n' * 3)

# ------------------------------------- #
# Math library examples
print('PI: {}'.format(math.pi))
print('E: {}'.format(math.e))
print('cos(pi / 2): {}'.format(math.cos(math.pi / 2)))
print('e ^ 2: {}'.format(math.exp(2)))
print('log (10) 100: {}'.format(math.log10(100)))
print('4!: {}'.format(math.factorial(4)))
# ------------------------------------- #

print('\n' * 3)

# ------------------------------------- #
# Random library examples
print('Random between 3 - 9: {}'.format(random.randrange(3,9)))

knights = ['Robin', 'Galahad', 'Lancelot', 'Sir Not Appearing In This Film']
print('Knights: {}'.format(knights))
print('Random knight: {}'.format(random.choice(knights)))
print('Shuffling list')
random.shuffle(knights)
print('Shuffled list: {}'.format(knights))
print('Random: {}'.format(random.random()))
# ------------------------------------- #
