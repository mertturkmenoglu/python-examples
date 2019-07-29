# Practice 002: Stack example


class Stack:

    def __init__(self, capacity):
        self.__capacity = capacity
        self.__elements = []
        self.__size = len(self.__elements)

    def push(self, element):
        if self.is_full():
            raise Exception

        self.__elements.append(element)
        self.__size = len(self.__elements)
        return True

    def pop(self):
        if self.is_empty():
            raise Exception

        value = self.__elements.pop()
        self.__size = len(self.__elements)

        return value

    def is_empty(self):
        return True if self.__size == 0 else False
    
    def is_full(self):
        return True if self.__size == self.__capacity else False

    def print_stack(self):
        print("---")
        for element in self.__elements:
            print(element)
        print("---")


s = Stack(5)
s.push(1)
s.push(2)
s.push(3)
s.push(4)
s.print_stack()
s.push(5)
s.print_stack()

# noinspection PyBroadException
try:
    s.push(6)
except Exception as e:
    print("Error on push operation")

for i in range(5):
    print("Value: ", s.pop())
    s.print_stack()

# noinspection PyBroadException
try:
    print("Value: ", s.pop())
except Exception as e:
    print("Error on pop operation")
