# Example 040: Polymorphism


class Triangle:
    
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return (self.base * self.height) / 2

    @staticmethod
    def draw():
        print("Drawing triangle")


class Square:
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

    @staticmethod
    def draw():
        print("Drawing square")


def print_area(s):
    print(s.area())


def draw_shape(s):
    s.draw()


shapes = [Triangle(10, 5), Square(7)]

for shape in shapes:
    print_area(shape)
    draw_shape(shape)
