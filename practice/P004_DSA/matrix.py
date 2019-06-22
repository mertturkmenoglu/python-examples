from util import connection


def createadjacencymatrix(wordlist):
    line_count = len(wordlist)
    matrix = [[False for i in range(line_count)] for i in range(line_count)]

    for i in range(line_count):
        for j in range(line_count):
            matrix[i][j] = False if i == j else connection(wordlist[i].word, wordlist[j].word)
            matrix[j][i] = matrix[i][j]

    return matrix


def printmatrix(matrix):
    for row in matrix:
        print(row)
    print()
