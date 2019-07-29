# Example 029: Matrix
import numpy
import random


def print_matrix(mtr):
    for index in range(len(mtr)):
        print(mtr[index])


row = int(input('Row: '))
col = int(input('Col: '))

matrix = [[0 for _ in range(col)] for _ in range(row)]

for i in range(row):
    for j in range(col):
        matrix[i][j] = random.randint(0, row * col)

print_matrix(matrix)

# Using numpy
arr = numpy.array([[1, 2, 3], [3, 4, 5]])
print_matrix(arr)
print_matrix(arr.transpose())
