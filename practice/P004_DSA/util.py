def check_neighbours(matrix, first, second):
    return matrix[first][second]


def check_neighbours_handler(matrix, word_list):

    first = input('Enter your first word: ')
    second = input('Enter your second word: ')

    first_index = get_index(word_list, first)
    second_index = get_index(word_list, second)

    if first_index == -1 or second_index == -1:
        raise ValueError

    result = check_neighbours(matrix, first_index, second_index)

    if result:
        print('{} and {} are neighbours'.format(first, second))
    else:
        print('{} and {} are not neighbours'.format(first, second))


def print_neighbours(matrix, word_list, index):
    word_count = len(word_list)

    for i in range(word_count):
        if matrix[index][i]:
            print(word_list[i].word)


def connection(first, second):
    first = str(first)
    second = str(second)

    actual_len = 5
    i = 0
    counter = 0

    while i < actual_len and counter < 2:
        if first[i] != second[i]:
            counter += 1
        i += 1

    return False if counter >= 2 else True


def connection_handler():
    first = input('Enter your first word: ')
    second = input('Enter your second word: ')

    result = connection(first, second)

    if result == 1:
        print("Same or one letter difference\n\n")
    else:
        print("More than one letter is different\n\n")


def get_index(word_list, string):
    for index, node in enumerate(word_list):
        result = string_compare(node.word, string)

        if result:
            return index

    return -1


def print_menu():
    print("---------------------------------------------------------------\n")
    print("1- Print Adjacency Matrix (First n element of connection matrix)\n")
    print("2- areTheyNeighbours (Give two words from matrix)\n")
    print("3- isDifferentOneLetter (Give any two words)\n")
    print("4- isTransformable (Is there any path between given two words)\n")
    print("5- printNeighbours (Print all 1-step transformations)\n")
    print("0- Exit\n")
    print("---------------------------------------------------------------\n")


def print_neighbours_handler(matrix, word_list):
    string = input('Enter your word')
    index = get_index(word_list, string)

    if index == -1:
        raise ValueError

    print_neighbours(matrix, word_list, index)


def string_compare(str1, str2):
    str1 = str(str1)
    str2 = str(str2)
    i = 0
    actual_len = 5

    while i < actual_len and str1[i] == str2[i]:
        i += 1

    return i == actual_len
