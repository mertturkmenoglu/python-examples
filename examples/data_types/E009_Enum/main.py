from enum import Enum


class Color(Enum):
    BLACK = (hex(0), hex(0), hex(0))
    RED = (hex(255), hex(0), hex(0))
    WHITE = (hex(255), hex(255), hex(255))


if __name__ == '__main__':
    print("Black: ", Color.BLACK.value)
    print("Red: ", Color.RED.value)
    print("White: ", Color.WHITE.value)
