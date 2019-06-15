# Example 017: Functions

# First comment like below is called documentation string
def sayHello(name):
    '''Prints Hello then the argument'''
    print('Hello {}'.format(name))

def findSquareArea(side_length):
    """Finds the area of a square with given
    side length"""
    if side_length > 0:
        return side_length * side_length
    else:
        return -1

print(sayHello.__doc__)
sayHello('John')

side_length = 5
area = findSquareArea(side_length)
print(area)