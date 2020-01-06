from algorithms.a_star.search import a_star

if __name__ == '__main__':
    grid = [[0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [1, 1, 1, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 1, 1, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    start = (0, 0)
    end = (7, 6)

    path = a_star(grid, start, end)

    # Print to console
    for i in range(10):
        for j in range(10):
            msg = None

            if (i, j) == start:
                msg = 's'
            elif (i, j) == end:
                msg = 'e'
            elif path is not None and (i, j) in path:
                msg = '.'
            else:
                msg = grid[i][j]

            print(msg, end=' ')

        print()
