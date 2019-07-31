import threading


def worker_function(index: int):
    print('{} - Worker'.format(index))


if __name__ == '__main__':
    threads = []
    n = 10

    for i in range(n):
        thread = threading.Thread(target=worker_function, args=[i])
        threads.append(thread)
        thread.start()
