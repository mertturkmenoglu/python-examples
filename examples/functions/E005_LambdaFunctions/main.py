# Using filter() and map() functions with lambdas

if __name__ == "__main__":
    numbers = [13, -1, -1, -1, 5, 7, -1, 4, -1, 17, 6, 9]
    numbers = list(filter(lambda it: it != -1, numbers))
    print(numbers)

    numbers = list(map(lambda it: it * 2, numbers))
    print(numbers)
