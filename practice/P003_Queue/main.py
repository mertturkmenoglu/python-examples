# Practice 003: Queue example

class Queue:

    def __init__(self, capacity):
        self.__capacity = capacity
        self.__elements = []
        self.__size = len(self.__elements)

    def enqueue(self, element):
        if (self.isFull()):
            raise Exception
            return False
        
        self.__elements.append(element)
        self.__size = len(self.__elements)
        return True

    def dequeue(self):
        if (self.isEmpty()):
            raise Exception

        self.__elements.reverse()
        value = self.__elements.pop()
        self.__elements.reverse()
        self.__size = len(self.__elements)

        return value

    def isEmpty(self):
        return True if self.__size == 0 else False
    
    def isFull(self):
        return True if self.__size == self.__capacity else False

    def printQueue(self):
        print("---")
        print(self.__elements)
        print("---")



q = Queue(5)
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.printQueue()
q.enqueue(5)
q.printQueue()

try:
    q.enqueue(6)
except Exception as e:
    print("Error on enqueue operation")

for i in range(5):
    print("Value: ", q.dequeue())
    q.printQueue()

try:
    print("Value: ", q.dequeue())
except Exception as e:
    print("Error on dequeue operation")