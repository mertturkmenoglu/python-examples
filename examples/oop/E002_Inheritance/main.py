# Example 038: Inheritance example


# Parent
class Shape:

    def __init__(self):
        print("Shape object created")

    def print_info(self):
        print("This is a Shape object")

    @staticmethod
    def draw():
        print("Drawing a Shape")


# A child class
class Triangle(Shape):

    def __init__(self):
        super().__init__()
        print("Triangle object created")

    def print_info(self):
        print("This is a Triangle object")

    @staticmethod
    def get_side_count():
        return 3


my_triangle = Triangle()
my_triangle.print_info()
my_triangle.draw()
print(my_triangle.get_side_count())
