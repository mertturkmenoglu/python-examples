# Example 043: Iterator

import time

class Odd:

    def __init__(self, begin = 1, end = 1):
        self.begin = begin
        self.end = end

    def __iter__(self):
        self.n = self.begin
        return self

    def __next__(self):
        if self.n <= self.end:
            result = self.n
            self.n += 2
            return result
        else:
            raise StopIteration


class InfEven:

    def __iter__(self):
        self.num = 0
        return self

    def __next__(self):
        num = self.num
        self.num += 2
        return num


for num in Odd(1, 17):
    print(num)

for num in InfEven():
    print(num)
    time.sleep(1)