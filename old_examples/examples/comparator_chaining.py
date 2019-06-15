# Comparator chaining example
# In Python, we can use multiple comparator
# operators in a single line. 


first_number = int(input('First number: ')) 
second_number = int(input('Second number: '))
third_number = int(input('Third number: '))

if first_number <= second_number <= third_number:
    print('Numbers are in order') 
else:
    print('Not in order')


