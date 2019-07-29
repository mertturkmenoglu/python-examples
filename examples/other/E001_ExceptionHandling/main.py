# Example 035: Exception Handling example
import sys

my_list = ['kadikoy', 3, 0, 'a', ]

for item in my_list:
    try:
        print("Item is: ", item)
        result = 42 / item
    except ArithmeticError:
        print("Exception: ", sys.exc_info()[0], " occured.")

numbers = [1, 3, 5, 7, 9]

try:
    for number in numbers:
        if number in my_list:
            raise ValueError('Value is in the list')
        else:
            print('Value is not in the list, search continues')
except ValueError as v_error:
    print(v_error)


try:
    file = open('text.txt', mode="r", encoding="utf-8")
    for line in file:
        print(line)
finally:
    file.close()
