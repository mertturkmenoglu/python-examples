# Example 039: Encapsulation

class Person:
    
    # dunder variables are "private"
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age


ali = Person("ali", 32)
print(ali.get_name())
print(ali.get_age())
