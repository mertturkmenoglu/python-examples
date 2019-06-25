# Practice 006: Identity Matrix
# Detect if a given matrix is identity matrix

def isIdentityMatrix(mtr: list) -> bool:
    row = len(mtr)
    col = len(mtr[0])

    if row != col:
        return False

    for i in range(row):
        for j in range(col):
            if i == j:
                if mtr[i][j] != 1:
                    return False
            elif mtr[i][j] != 0:
                return False

    return True

mtr1 = [
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1]
]

mtr2 = [
    [1, 1, 0],
    [0, 1, 0],
    [0, 0, 1]
]

print(isIdentityMatrix(mtr1))
print(isIdentityMatrix(mtr2))