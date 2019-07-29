# Example 012: For loop example

# Lets have a list of some of the prime numbers
prime_numbers = [2, 3, 5, 7]
# And a random number list
my_numbers = [2, 1, 4, 6, 3]

# For loop is technically for-each loop in other languages
# You iterate over an iterable. It is actually a while(True) loop
# behind but it is more complicated

# iterate over my_numbers and on each step, assign the value to variable
# number
for number in my_numbers:
    if number in prime_numbers:
        print('My number {} is prime'.format(number))
    else:
        print('My number {} is not prime'.format(number))

# When you need a classic for loop with an index goes from 0 to number n
# can use the built-in range function. It produces a number collection
# and iterates over it
for i in range(10):
    print(i)

print('----')

# Other use of range function
for i in range(3, 6):
    print(i)

print('----')

# Different step count
for i in range(0, 10, 2):
    print(i)

# Reverse iteration is possible
for i in reversed(range(0, 10, 2)):
    print(i)

# A unique feature of for loop. You can else branch for a for loop
for i in range(0, 3):
    print('{} is in range'.format(i))
else:
    print('For loop is over')

print('After for loop')
