# Practice 001: Read and print matrix

row = int(input('Row number: '))
col = int(input('Col number: '))

matrix = [[0 for i in range(col)] for i in range(row)]
print(matrix)
