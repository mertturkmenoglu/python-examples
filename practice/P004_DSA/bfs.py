import data
from util import *


def bfs(matrix, wordlist, start, end):
    for word in wordlist:
        word.level = 0
        word.parent = None

    q = data.Queue(10000)
    q.enqueue(wordlist[start])

    visited = [False for i in range(len(wordlist))]
    visited[start] = True

    while not q.isempty():
        dequed = q.dequeue()
        v = dequed

        result = stringcompare(wordlist[end].word, v.word)

        if result:
            path = data.Path([None for i in range(v.level + 1)], v.level + 1, v.level)

            j = v.level
            while v is not None:
                path.path[j] = getindex(wordlist, v.word)
                v = v.parent
                j -= 1

            return path

        index = getindex(wordlist, v.word)

        for i in range(len(wordlist)):
            if matrix[index][i] and visited[i] is False:
                visited[i] = True
                wordlist[i].level = v.level + 1
                wordlist[i].parent = v
                q.enqueue(wordlist[i])

    return None


def bfshandler(matrix, wordlist):

    first = input('Enter your first word: ')
    second = input('Enter your second word: ')

    start = getindex(wordlist, first)
    end = getindex(wordlist, second)

    if start == -1 or end == -1:
        raise ValueError

    result = bfs(matrix, wordlist, start, end)
    if result is not None:
        print('There is a transformation between {} and {}: {} steps'.format(first, second, result.step))
        for i in range(result.n):
            print(wordlist[result.path[i]].word)
    else:
        print('There is no transformation between {} and {}'.format(first, second))

    print('--------------------------\n\n')
