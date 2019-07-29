# Example 048: Variable length arguments


def find_max(*argv):
    maxx = argv[0]
    for arg in argv:
        if arg > maxx:
            maxx = arg

    return maxx


if __name__ == "__main__":
    max1 = find_max(3, 5, 1, -1)
    max2 = find_max(-1, -7, -12, -16)

    print(max1)
    print(max2)
