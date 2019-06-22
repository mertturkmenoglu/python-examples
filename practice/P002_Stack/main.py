# Practice 002: Stack example

class Stack:

    def __init__(self, capacity):
        self.__capacity = capacity
        self.__elements = []
        self.__size = len(self.__elements)

    def push(self, element):
        if (self.isFull()):
            raise Exception
            return False
        
        self.__elements.append(element)
        self.__size = len(self.__elements)
        return True

    def pop(self):
        if (self.isEmpty()):
            raise Exception

        value = self.__elements.pop()
        self.__size = len(self.__elements)

        return value

    def isEmpty(self):
        return True if self.__size == 0 else False
    
    def isFull(self):
        return True if self.__size == self.__capacity else False

    def printStack(self):
        print("---")
        for i in self.__elements:
            print(i)
        print("---")


s = Stack(5)
s.push(1)
s.push(2)
s.push(3)
s.push(4)
s.printStack()
s.push(5)
s.printStack()

try:
    s.push(6)
except Exception as e:
    print("Error on push operation")

for i in range(5):
    print("Value: ", s.pop())
    s.printStack()

try:
    print("Value: ", s.pop())
except Exception as e:
    print("Error on pop operation")