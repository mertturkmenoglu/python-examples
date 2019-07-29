import data
from util import *


def bfs(matrix, word_list, start, end):
    for word in word_list:
        word.level = 0
        word.parent = None

    q = data.Queue(10000)
    q.enqueue(word_list[start])

    visited = [False for _ in range(len(word_list))]
    visited[start] = True

    while not q.is_empty():
        dequed = q.dequeue()
        v = dequed

        result = string_compare(word_list[end].word, v.word)

        if result:
            path = data.Path([None for _ in range(v.level + 1)], v.level + 1, v.level)

            j = v.level
            while v is not None:
                path.path[j] = get_index(word_list, v.word)
                v = v.parent
                j -= 1

            return path

        index = get_index(word_list, v.word)

        for i in range(len(word_list)):
            if matrix[index][i] and visited[i] is False:
                visited[i] = True
                word_list[i].level = v.level + 1
                word_list[i].parent = v
                q.enqueue(word_list[i])

    return None


def bfs_handler(matrix, word_list):

    first = input('Enter your first word: ')
    second = input('Enter your second word: ')

    start = get_index(word_list, first)
    end = get_index(word_list, second)

    if start == -1 or end == -1:
        raise ValueError

    result = bfs(matrix, word_list, start, end)
    if result is not None:
        print('There is a transformation between {} and {}: {} steps'.format(first, second, result.step))
        for i in range(result.n):
            print(word_list[result.path[i]].word)
    else:
        print('There is no transformation between {} and {}'.format(first, second))

    print('--------------------------\n\n')
