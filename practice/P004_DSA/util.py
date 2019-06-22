def checkNeighbours(matrix, first, second):
    return matrix[first][second]


def checkNeighboursHandler(matrix, wordlist):

    first = input('Enter your first word: ')
    second = input('Enter your second word: ')

    firstIndex = getindex(wordlist, first)
    secondIndex = getindex(wordlist, second)

    if firstIndex == -1 or secondIndex == -1:
        raise ValueError

    result = checkNeighbours(matrix, firstIndex, secondIndex)

    if result:
        print('{} and {} are neighbours'.format(first, second))
    else:
        print('{} and {} are not neighbours'.format(first, second))


def printNeighbours(matrix, wordlist, index):
    wordCount = len(wordlist)

    for i in range(wordCount):
        if matrix[index][i]:
            print(wordlist[i].word)


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


def connectionHandler():
    first = input('Enter your first word: ')
    second = input('Enter your second word: ')

    result = connection(first, second)

    if result == 1:
        print("Same or one letter difference\n\n")
    else:
        print("More than one letter is different\n\n")


def getindex(wordlist, string):
    for index, node in enumerate(wordlist):
        result = stringcompare(node.word, string)

        if result:
            return index

    return -1

def printmenu():
    print("---------------------------------------------------------------\n")
    print("1- Print Adjacency Matrix (First n element of connection matrix)\n")
    print("2- areTheyNeighbours (Give two words from matrix)\n")
    print("3- isDifferentOneLetter (Give any two words)\n")
    print("4- isTransformable (Is there any path between given two words)\n")
    print("5- printNeighbours (Print all 1-step transformations)\n")
    print("0- Exit\n")
    print("---------------------------------------------------------------\n")


def printneighbourshandler(matrix, wordlist):
    string = input('Enter your word')
    index = getindex(wordlist, string)

    if index == -1:
        raise ValueError

    printNeighbours(matrix, wordlist, index)


def stringcompare(str1, str2):
    str1 = str(str1)
    str2 = str(str2)
    i = 0
    actual_len = 5

    while i < actual_len and str1[i] == str2[i]:
        i += 1

    return i == actual_len
