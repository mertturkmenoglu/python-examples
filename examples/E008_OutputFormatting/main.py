# Example 008: Output formatting

x = 3
y = 4

print('Point: {} - {}'.format(x, y))
print('x: {x}\ty: {y}'.format(x = x,y = y))
print('%d - %d' %(x, y))

first = int(input('Enter the first integer: '))
second = int(input('Enter the second integer: '))

print('You entered {} and {}'.format(first, second))