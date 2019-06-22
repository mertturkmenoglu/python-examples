# Example 044: Generators

def evenrange(begin=0, end=0):
    if (begin % 2 == 0):
        yield begin
    else:
        begin += 1
        yield begin

    while (begin < end):
        begin += 2
        yield begin


for i in evenrange(4, 18):
    print(i)

# Generator expression
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
gen_exp = (i % 2 for i in numbers)

print(next(gen_exp))