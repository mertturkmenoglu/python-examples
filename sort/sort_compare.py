import time
from random import randint
from bubble_sort import bubble_sort
from selection_sort import selection_sort
from insertion_sort import insertion_sort

array = []
n = 10000

for i in range(n):
    array.append(randint(0, n))

tempList = array.copy()
startTime = time.asctime()
print('Bubble sort started: ')
print(startTime)
bubble_sort(tempList, n)
endTime = time.asctime()
print('Bubble sort ended: ')
print(endTime)

tempList = array.copy()
startTime = time.asctime()
print('Selection sort started: ')
print(startTime)
selection_sort(tempList, n)
endTime = time.asctime()
print('Selection sort ended: ')
print(endTime)

tempList = array.copy()
startTime = time.asctime()
print('Insertion sort started: ')
print(startTime)
insertion_sort(tempList, n)
endTime = time.asctime()
print('Insertion sort ended: ')
print(endTime)
