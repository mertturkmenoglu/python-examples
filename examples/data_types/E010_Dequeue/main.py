from collections import deque

if __name__ == '__main__':
    q = deque([])
    print(q)

    q.append(1)
    print(q)

    q.append(2)
    q.append(3)
    print(q)

    q.popleft()
    print(q)

    q.popleft()
    print(q)
