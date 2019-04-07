import time
from random import randint

array = []
n = 10000

for i in range(n):
    array.append(randint(0, n))

startTime = time.asctime()
print('Sorting started: ')
print(startTime)

for i in range(n-1):
    for j in range(n-1-i):
        if(array[j] > array[j+1]):
            array[j], array[j+1] = array[j+1], array[j]

endTime = time.asctime()
print('Sorting ended: ')
print(endTime)
