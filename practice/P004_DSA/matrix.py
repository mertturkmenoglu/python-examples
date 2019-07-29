from util import connection


def create_adjacency_matrix(word_list):
    line_count = len(word_list)
    matrix = [[False for _ in range(line_count)] for _ in range(line_count)]

    for i in range(line_count):
        for j in range(line_count):
            matrix[i][j] = False if i == j else connection(word_list[i].word, word_list[j].word)
            matrix[j][i] = matrix[i][j]

    return matrix


def print_matrix(matrix):
    for row in matrix:
        print(row)
    print()
