from random import shuffle

def bogo_sort(array, n):
    a = False
    while(a != True):
        shuffle(array)
        i = 0
        a = all(array[i] <= array[i+1] for i in range(len(array)-1))
    return array
