# Example 024: List

# ------------------------------------------------ #
# Create different type lists
empty_list = []
integer_list = [1, 2, 3]
mixed_list = [42, 3.14, 'Ni!']
nested_list = [1, 2, integer_list]
# ------------------------------------------------ #



# ------------------------------------------------ #
# Print lists
print('Printing lists')
print('Empty list: {}'.format(empty_list))
print('One data type list: {}'.format(integer_list))
print('Mixed data type list: {}'.format(mixed_list))
print('Nested list: {}'.format(nested_list))
# ------------------------------------------------ #

print('\n' * 3)

# ------------------------------------------------ #
# Access via index
print('Indexing')
print('integer_list[0]: {}'.format(integer_list[0]))
print('mixed_list[1]: {}'.format(mixed_list[1]))
print('mixed_list[2]: {}'.format(mixed_list[2]))
print('nested_list[2][1]: {}'.format(nested_list[2][1]))
# ------------------------------------------------ #

print('\n' * 3)

# ------------------------------------------------ #
# Negative indexing
print('Negative Indexing')
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print('numbers: {}'.format(numbers))
print('numbers[8]: {}'.format(numbers[8]))
print('numbers[-2]: {}'.format(numbers[-2]))
# ------------------------------------------------ #

print('\n' * 3)

# ------------------------------------------------ #
# Slicing
print('Slicing Examples')
print('numbers[2:5]: {}'.format(numbers[2:5]))
print('numbers[:-5]: {}'.format(numbers[:-5]))
print('numbers[5:]: {}'.format(numbers[5:]))
print('numbers[:]: {}'.format(numbers[:]))
# ------------------------------------------------ #

print('\n' * 3)

# ------------------------------------------------ #
# They are mutable
print('Changing Elements')
print(numbers)
print('numbers[0] = 9')
numbers[0] = 9
print('After: {}'.format(numbers))

print('numbers[1:10] = [8, 7, 6, 5, 4, 3, 2, 1, 0]')
numbers[1:10] = [8, 7, 6, 5, 4, 3, 2, 1, 0]
print('After: {}'.format(numbers))
# ------------------------------------------------ #

print('\n' * 3)

# ------------------------------------------------ #
# Appending and extending
print('List.append() and List.extend() methods')
numbers = [0, 1, 2]
print('Numbers: {}'.format(numbers))

numbers.append(3)
print('After appending: {}'.format(numbers))

numbers.extend([4, 5, 6, 7, 8, 9])
print('After extending: {}'.format(numbers))
# ------------------------------------------------ #

print('\n' * 3)

# ------------------------------------------------ #
# Operators
print("Operators")
message = ["We", "are", "the", "knights"]
print('Message: {}'.format(message))
message += ["who", "say", "Ni!"]
print('After: {}'.format(message))

message = ["Ni!"] * 5
print('Message: {}'.format(message))

message = ["We", "are", "knights", "who"]
print('Message: {}'.format(message))
message.insert(2, "the")
print('After insert: {}'.format(message))
# ------------------------------------------------ #

print('\n' * 3)

# ------------------------------------------------ #
# Deleting
print('Deleting')
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print('Numbers: {}'.format(numbers))
print('Delete numbers[2]')
del numbers[2]
print('Numbers: {}'.format(numbers))
print('Delete numbers[1:5]')
del numbers[1:5]
print('Numbers: {}'.format(numbers))
print('Delete whole list')
del numbers
# ------------------------------------------------ #

print('\n' * 3)

# ------------------------------------------------ #
# List methods
print('List Methods Example')
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print('Numbers: {}'.format(numbers))
numbers.remove(3)
print('After remove(3): {}'.format(numbers))
print('numbers.pop(1): {}'.format(numbers.pop(1)))
print('After pop(1): {}'.format(numbers))
print('numbers.pop(): {}'.format(numbers.pop()))
print('After pop(): {}'.format(numbers))

numbers = [2, 1, 4, 7, 6, 6, 3, 3, 3, 5]
print('New numbers: {}'.format(numbers))
print('numbers.index(3): {}'.format(numbers.index(3)))
print('numbers.count(3): {}'.format(numbers.count(3)))
numbers.sort()
print('Sort: {}'.format(numbers))
numbers.reverse()
print('Reverse: {}'.format(numbers))
# ------------------------------------------------ #

print('\n' * 3)

# ------------------------------------------------ #
# List comprehensions
print('List comprehensions')
even = [i for i in range(10) if i % 2 == 0]
print('Even numbers: {}'.format(even))

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print('7 in numbers: {}'.format(7 in numbers))
print('13 in numbers: {}'.format(13 in numbers))
print('13 not in numbers: {}'.format(13 not in numbers))

knights = ['Robin', 'Galahad', 'Lancelot', 'Sir Not Appearing In This Film']

for knight in knights:
    print('{} is a knight!'.format(knight))
# ------------------------------------------------ #