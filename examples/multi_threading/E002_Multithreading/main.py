import threading
import time


def print_message(thread_name: str, message: str):
    print("Current thread: ", threading.current_thread().name)
    counter = 0

    while counter < 50:
        counter += 1
        print("Thread: {}\tTime: {}\tMessage: {}".format(thread_name, time.ctime(time.time()), message))


def print_numbers(thread_name: str, begin: int = 0, end: int = 0):
    print("Current thread: ", threading.current_thread().name)

    for i in range(begin, end):
        print("Thread: {}\tTime: {}\tMessage: {}".format(thread_name, time.ctime(time.time()), i))


if __name__ == '__main__':
    thread1 = threading.Thread(target=print_message, name="first", args=["thread1", "Ni!"])
    thread2 = threading.Thread(target=print_numbers, name="second", args=["thread2", 5, 50])

    print("Current thread: ", threading.current_thread().name)

    thread1.start()
    thread2.start()

    threads = [thread1, thread2]

    for thread in threads:
        thread.join()
