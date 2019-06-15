import time
array = []
n = 100000
for i in range(n):
    array.append(i+1)
array.reverse()
startTime = time.asctime()
print('Islem basladi: ')
print(startTime)
for i in range(n-1):
    min_index = i
    for j in range(i+1, n):
        if(array[j] < array[min_index]):
            min_index = j
    array[min_index], array[i] = array[i], array[min_index]
endTime = time.asctime()
print('Islem bitti: ')
print(endTime)