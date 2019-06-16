# Example 038: Inheritance exaxmple

# Parent
class Shape:

    def __init__(self):
        print("Shape object created")

    def printInfo(self):
        print("This is a Shape object")

    def draw(self):
        print("Drawing a Shape")

# A child class
class Triangle(Shape):

    def __init__(self):
        super().__init__()
        print("Triangle object created")

    def printInfo(self):
        print("This is a Triangle object")

    def get_side_count(self):
        return 3

my_triangle = Triangle()
my_triangle.printInfo()
my_triangle.draw()
print(my_triangle.get_side_count())
