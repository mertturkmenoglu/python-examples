# Example 047: Multithreading example

import threading


def print_numbers():
    for i in range(50):
        print(i)


def print_message():
    for i in range(50):
        print("Ni!")


if __name__ == '__main__':
    t1 = threading.Thread(target=print_numbers)
    t2 = threading.Thread(target=print_message)

    t1.start()
    t2.start()
