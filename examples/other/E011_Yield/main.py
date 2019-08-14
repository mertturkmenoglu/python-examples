def even_numbers(begin, end):
    def is_even(n):
        return n % 2 == 0

    if not is_even(begin):
        begin += 1

    if not is_even(end):
        end -= 1

    while begin <= end:
        yield begin
        begin += 2


if __name__ == '__main__':
    for e in even_numbers(0, 10):
        print(e)
