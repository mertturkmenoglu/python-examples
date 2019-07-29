# Example 020: Lambda(anonymous) function example

lambda_function = lambda num: num + 1

print(lambda_function(3))

# From list numbers filter positive numbers and return a collection
# Cast it to a list and assign it to positive_numbers
numbers = [-3, 1, 0, 2, -4, 8, 13, -11]
positive_numbers = list(filter(lambda x: (x > 0), numbers))

print('Numbers: {}'.format(numbers))
print('Positive numbers: {}'.format(positive_numbers))

# From list numbers increase all numbers by one and return a collection
# Cast it to a list and assign it to increased_numbers
increased_numbers = list(map(lambda x: x + 1, numbers))

print('Numbers: {}'.format(numbers))
print('Increased numbers: {}'.format(increased_numbers))
