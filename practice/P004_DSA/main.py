# Practice 004: Data Structures and Algorithms
# Semester Project Python implementation

from bfs import *
from matrix import *
from util import *


file_path = input('Enter file path: ')
word_list = []


with open(file_path, encoding='utf-8', mode="r+") as file:
    for line in file:
        word_list.append(data.Node(line, 0, None))

line_count = len(word_list)
mtr = createadjacencymatrix(word_list)

while True:
    printmenu()
    choice = int(input('Enter your choice'))
    operation = None

    if choice == 1:
        printmatrix(mtr)
    elif choice == 2:
        checkNeighboursHandler(mtr, word_list)
    elif choice == 3:
        connectionHandler()
    elif choice == 4:
        bfshandler(mtr, word_list)
    elif choice == 5:
        printneighbourshandler(mtr, word_list)
    elif choice == 0:
        break
    else:
        raise ValueError
