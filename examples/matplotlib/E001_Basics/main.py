import matplotlib.pyplot as mpl


def fib(n: int) -> list:
    a = 1
    b = 1
    result = [a, b]

    for i in range(3, n):
        c = a + b
        result.append(c)
        a = b
        b = c

    return result


if __name__ == '__main__':
    y_values = fib(10)
    x_values = [i + 1 for i in range(len(y_values))]

    mpl.plot(x_values, y_values)
    mpl.xlabel('No')
    mpl.ylabel('Values')

    mpl.show()
