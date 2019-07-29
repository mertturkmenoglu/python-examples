# Example 009: Special operators example

# Python has some special operators.
# is - is not - in - not in

# Lets create three lists
first_list = ['Robin', 'Galahad', 'Lancelot']
second_list = ['Robin', 'Galahad', 'Lancelot']
third_list = ['Galahad', 'Robin', 'Lancelot']

# Check if every element is same in both list
print(first_list is second_list)
print(first_list is third_list)

# Check if not every element matches
print(first_list is not third_list)

# Check if given element is in the list(collection)
print('Robin' in first_list)

# Check if given element is not in the list(collection)
print('King Arthur' not in first_list)


# Compare objects
name1 = 'Sherlock'
name2 = 'Sherlock'
print(name1 is name2)
