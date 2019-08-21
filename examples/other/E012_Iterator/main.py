from itertools import takewhile


class ExponentialSequence:

    def __init__(self):
        self.value = 0

    def __next__(self):
        self.value += 1
        return self.value ** self.value

    def __iter__(self):
        return self


if __name__ == '__main__':
    es = ExponentialSequence()
    numbers = takewhile(lambda x: x < 10_000, es)

    for n in numbers:
        print(n)
