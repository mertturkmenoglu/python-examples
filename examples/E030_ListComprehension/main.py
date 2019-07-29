# Example 030: List comprehensions


def get_transpose(mtr):
    result = []

    for i in range(len(mtr[0])):
        transposed_row = []

        for row in mtr:
            transposed_row.append(row[i])
        result.append(transposed_row)

    return result


letters = [letter for letter in 'kadikoy']
print(letters)

letters = list(map(lambda letter: letter, 'kadikoy'))
print(letters)

odd_numbers = [i for i in range(10) if i % 2 == 1]
print(odd_numbers)

special_numbers = [i for i in range(100) if i % 5 == 0 if i % 6 == 0]
print(special_numbers)

even_numbers = [True if i % 2 == 0 else False for i in range(10)]
print(even_numbers)

matrix = [[1, 2], [3, 4], [5, 6], [7, 8]]
transpose = get_transpose(matrix)
print(transpose)
