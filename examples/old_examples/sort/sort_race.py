import time
from random import randint
from bubble_sort import bubble_sort
from selection_sort import selection_sort
from insertion_sort import insertion_sort


n = 1000


def find_winner():
    array = []
    for _ in range(n):
        array.append(randint(0, n))

    temp_list = array.copy()
    bubble_start_time = time.time()
    bubble_sort(temp_list, n)
    bubble_end_time = time.time()
    bubble_complete_time = bubble_end_time - bubble_start_time

    temp_list = array.copy()
    selection_start_time = time.time()
    selection_sort(temp_list, n)
    selection_end_time = time.time()
    selection_complete_time = selection_end_time - selection_start_time

    temp_list = array.copy()
    insertion_start_time = time.time()
    insertion_sort(temp_list, n)
    insertion_end_time = time.time()
    insertion_complete_time = insertion_end_time - insertion_start_time

    temp_list = array.copy()
    python_sort_start_time = time.time()
    sorted(temp_list)
    python_sort_end_time = time.time()
    python_sort_complete_time = python_sort_end_time - python_sort_start_time

    print(bubble_complete_time)
    print(selection_complete_time)
    print(insertion_complete_time)
    print(python_sort_complete_time)
    print('One cycle ended')

    time_arr = [bubble_complete_time, selection_complete_time, insertion_complete_time, python_sort_complete_time]
    return find_min_index(time_arr)


def find_min_index(array):
    min_index = 0
    for _ in range(1, len(array)):
        if array[i] < array[min_index]:
            min_index = i
    return min_index


winners = [0, 0, 0, 0]

for i in range(10000):
    j = find_winner()
    print('Winner: %d' % j)
    winners[j] += 1

print(winners)
