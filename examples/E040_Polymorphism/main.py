# Example 040: Polymorphism

class Triangle:
    
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return (self.base * self.height) / 2

    def draw(self):
        print("Drawing triangle")


class Square:
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

    def draw(self):
        print("Drawing square")


def printArea(shape):
    print(shape.area())


def drawShape(shape):
    shape.draw()


shapes = []
shapes.append(Triangle(10, 5))
shapes.append(Square(7))

for shape in shapes:
    printArea(shape)
    drawShape(shape)

