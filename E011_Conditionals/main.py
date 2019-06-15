# Example 011: Conditional statements example

age = 30

if age >= 18:
    print('You are an adult')

characters = ['sherlock', 'watson', 'moriarty']

if 'bond' in characters:
    print('It is in Sherlock Holmes series')
else:
    print('Bond is not in Sherlock Holmes series')

number = -2

if number > 0:
    print('Number is positive')
elif number < 0:
    print('Number is negative')
else:
    print('Number is zero')

first_list = [1, 2, 3]
second_list = [3, 4, 5]

number = 3

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
