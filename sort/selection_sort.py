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
    location = i
    min = array[i]
    for j in range(i+1, n):
        if(array[j] < min):
            min = array[j]
            location = j
    array[location] = array[i]
    array[i] = min
    
endTime = time.asctime()
print('Sorting ended: ')
print(endTime)
