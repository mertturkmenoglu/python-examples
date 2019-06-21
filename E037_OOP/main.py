# Example 037: Object Oriented Programming example

class Person:
    # Class attribute
    planet = "earth"

    # Constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Methods
    def get_old(self, year):
        self.age += year

    def get_infos(self):
        return "Name: {} Age: {}".format(self.name, self.age)

# Create objects
p1 = Person("John", 47)
p2 = Person("Emily", 32)

print("John's planet: {}".format(p1.__class__.planet))
print("Emily's planet: {}".format(p2.__class__.planet))

p1.__class__.planet = "mars"

print("John's planet: {}".format(p1.__class__.planet))
print("Emily's planet: {}".format(p2.__class__.planet))

print("{} is {} years old".format(p1.name, p1.age))
print("{} is {} years old".format(p2.name, p2.age))

print(p1.get_infos())
p1.get_old(10)
print(p1.get_infos())