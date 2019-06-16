# Example 029: Matrix
import numpy
import random

def printMatrix(mtr):
    for i in range(len(mtr)):
        print(mtr[i])

row = int(input('Row: '))
col = int(input('Col: '))

matrix = [[0 for i in range(col)] for i in range(row)]

for i in range(row):
    for j in range(col):
        matrix[i][j] = random.randint(0, row * col)

printMatrix(matrix)

# Using numpy
arr = numpy.array([[1, 2, 3], [3, 4, 5]])
printMatrix(arr)
printMatrix(arr.transpose())