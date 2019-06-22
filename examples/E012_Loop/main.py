# Example 012: For loop example

prime_numbers = [2, 3, 5, 7]

my_numbers = [2, 1, 4, 6, 3]

for number in my_numbers:
    if number in prime_numbers:
        print('My number {} is prime'.format(number))
    else:
        print('My number {} is not prime'.format(number))

for i in range(10):
    print(i)

print('----')

for i in range(3, 6):
    print(i)

print('----')

for i in range(0, 10, 2):
    print(i)

for i in range(0, 3):
    print('{} is in range'.format(i))
else:
    print('For loop is over')

print('After for loop')
