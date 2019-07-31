import threading
import time


def worker():
    print("Start --- Thread name: ", threading.currentThread().getName())
    time.sleep(2)
    print("End ----- Thread name: ", threading.current_thread().getName())


def service_function():
    print("Start --- Thread name: ", threading.current_thread().getName())
    time.sleep(3)
    print("End ----- Thread name: ", threading.current_thread().getName())


if __name__ == '__main__':
    service = threading.Thread(name='service_function', target=service_function)
    worker1 = threading.Thread(name='worker', target=worker)
    worker2 = threading.Thread(target=worker)

    worker1.start()
    worker2.start()
    service.start()
