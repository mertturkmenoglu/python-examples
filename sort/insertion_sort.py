import time
from random import randint

array = []
n = 10000

for i in range(n):
    array.append(randint(0, n))

startTime = time.asctime()
print('Sorting started: ')
print(startTime)

for i in range(n):
    j = i - 1
    temp = array[i]
    while(j >= 0 and array[j] > temp):
        array[j+1] = array[j]
        j -= 1
    array[j+1] = temp

endTime = time.asctime()
print('Sorting ended: ')
print(endTime)
