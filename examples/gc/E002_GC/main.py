import time


class Testing:
    def __init__(self):
        print("Init")

    def __del__(self):
        print("Destruct")

    @staticmethod
    def hi():
        print("hi")


obj = Testing()
obj.hi()
obj = None

time.sleep(10)
