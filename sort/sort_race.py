import time
from random import randint
from bubble_sort import bubble_sort
from selection_sort import selection_sort
from insertion_sort import insertion_sort

n = 1000

def findWinner():
    array = []
    for i in range(n):
        array.append(randint(0, n))

    tempList = array.copy()
    bubbleStartTime = time.time()
    bubble_sort(tempList, n)
    bubbleEndTime = time.time()
    bubbleCompleteTime = bubbleEndTime - bubbleStartTime

    tempList = array.copy()
    selectionStartTime = time.time()
    selection_sort(tempList, n)
    selectionEndTime = time.time()
    selectionCompleteTime = selectionEndTime - selectionStartTime

    tempList = array.copy()
    insertionStartTime = time.time()
    insertion_sort(tempList, n)
    insertionEndTime = time.time()
    insertionCompleteTime = insertionEndTime - insertionStartTime

    tempList = array.copy()
    pythonSortStartTime = time.time()
    sorted(tempList)
    pythonSortEndTime = time.time()
    pythonSortCompleteTime = pythonSortEndTime - pythonSortStartTime

    print(bubbleCompleteTime)
    print(selectionCompleteTime)
    print(insertionCompleteTime)
    print(pythonSortCompleteTime)
    print('One cycle ended')

    timeArray = []
    timeArray.append(bubbleCompleteTime)
    timeArray.append(selectionCompleteTime)
    timeArray.append(insertionCompleteTime)
    timeArray.append(pythonSortCompleteTime)
    return findMinIndex(timeArray)


def findMinIndex(array):
    min = 0
    for i in range(1, len(array)):
        if(array[i] < array[min]):
            min = i
    return min


winners = [0, 0, 0, 0]

for i in range(10000):
    j = findWinner()
    print('Winner: %d'%j)
    winners[j] += 1

print(winners)
