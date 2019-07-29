# Practice 001: Read and print matrix

row = int(input('Row number: '))
col = int(input('Col number: '))

matrix = [[0 for _ in range(col)] for _ in range(row)]
print(matrix)
