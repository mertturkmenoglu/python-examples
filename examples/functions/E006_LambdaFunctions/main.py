def for_each(f: callable, l: list) -> None:
    for e in l:
        f(e)


if __name__ == "__main__":
    numbers = [3, 4, 5, 6]
    for_each(lambda x: print(x, end='\t'), numbers)
    print()
    for_each(lambda x: print(x ** 2, end='\t'), numbers)
