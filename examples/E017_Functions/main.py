# Example 017: Functions


# First comment like below is called documentation string
def say_hello(name):
    """Prints Hello then the argument"""
    print('Hello {}'.format(name))


def find_square_area(s_length):
    """Finds the area of a square with given
    side length"""
    if s_length > 0:
        return s_length * s_length
    else:
        return -1


print(say_hello.__doc__)
say_hello('John')

side_length = 5
area = find_square_area(side_length)
print(area)
