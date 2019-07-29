# Example 011: Conditional statements example

# Create a variable
age = 30

# Check if the value is greater or equal to 18
# If it satisfies the condition, then execute the indented code below
# Otherwise, continue to normal program execution flow
if age >= 18:
    print('You are an adult')

characters = ['sherlock', 'watson', 'moriarty']

# Check if element is in the list
# If so, execute given code
# Otherwise execute the code in the else branch.
# Then continue to normal program execution flow
if 'bond' in characters:
    print('It is in Sherlock Holmes series')
else:
    print('Bond is not in Sherlock Holmes series')

number = -2

# Nested condition check. Similar approach.
if number > 0:
    print('Number is positive')
elif number < 0:
    print('Number is negative')
else:
    print('Number is zero')

first_list = [1, 2, 3]
second_list = [3, 4, 5]

number = 3

# You can use elif keyword or you can use nested if else 
# branching. This is a general approach but elif is the Python way.
if number in first_list:
    if number in second_list:
        print('Number is in both of the lists')
    else:
        print('Number is just in the first list')
else:
    if number in second_list:
        print('Number is just in the second list')
    else:
        print('Can not find the number in lists')
