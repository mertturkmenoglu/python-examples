# Example 041: Method Resolution Order example

class Man:
    pass

class Woman:
    pass

class Child(Woman, Man):
    pass


print(Child.mro())
