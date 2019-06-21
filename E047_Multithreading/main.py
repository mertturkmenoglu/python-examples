# Example 047: Multithreading example

import threading


def printNumbers():
    for i in range(50):
        print(i)


def printMessage():
    for i in range(50):
        print("Ni!")


t1 = threading.Thread(target=printNumbers)
t2 = threading.Thread(target=printMessage)

t1.start()
t2.start()