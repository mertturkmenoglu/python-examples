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
mtr = create_adjacency_matrix(word_list)

while True:
    print_menu()
    choice = int(input('Enter your choice'))
    operation = None

    if choice == 1:
        print_matrix(mtr)
    elif choice == 2:
        check_neighbours_handler(mtr, word_list)
    elif choice == 3:
        connection_handler()
    elif choice == 4:
        bfs_handler(mtr, word_list)
    elif choice == 5:
        print_neighbours_handler(mtr, word_list)
    elif choice == 0:
        break
    else:
        raise ValueError
