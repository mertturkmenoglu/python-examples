# Example 042: Operator Overloading


class Vector2D:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "x: {} y: {}".format(self.x, self.y)

    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector2D(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return self.x * other.x + self.y * other.y

    def __truediv__(self, value):
        return Vector2D(self.x / value, self.y / value)

    def __floordiv__(self, value):
        return Vector2D(self.x // value, self.y // value)

    def __invert__(self):
        return Vector2D(-self.x, -self.y)

    def __lt__(self, other):
        self_magnitude = (self.x ** 2) + (self.y ** 2)
        other_magnitude = (other.x ** 2) + (other.y ** 2)

        return self_magnitude < other_magnitude

    def __le__(self, other):
        self_magnitude = (self.x ** 2) + (self.y ** 2)
        other_magnitude = (other.x ** 2) + (other.y ** 2)

        return self_magnitude <= other_magnitude

    def __eq__(self, other):
        self_magnitude = (self.x ** 2) + (self.y ** 2)
        other_magnitude = (other.x ** 2) + (other.y ** 2)

        return self_magnitude == other_magnitude

    def __ne__(self, other):
        self_magnitude = (self.x ** 2) + (self.y ** 2)
        other_magnitude = (other.x ** 2) + (other.y ** 2)

        return self_magnitude != other_magnitude

    def __gt__(self, other):
        self_magnitude = (self.x ** 2) + (self.y ** 2)
        other_magnitude = (other.x ** 2) + (other.y ** 2)

        return self_magnitude > other_magnitude

    def __ge__(self, other):
        self_magnitude = (self.x ** 2) + (self.y ** 2)
        other_magnitude = (other.x ** 2) + (other.y ** 2)

        return self_magnitude >= other_magnitude


v1 = Vector2D(3, 4)
v2 = Vector2D(5, 12)

print(v1)
print(v2)
print(v1 + v2)
print(v1 - v2)
print(v1 * v2)
print(v1 / 2)
print(v2 // 2)
print(~v1)
print(v1 < v2)
print(v1 <= v2)
print(v1 == v2)
print(v1 != v2)
print(v1 > v2)
print(v1 >= v2)
