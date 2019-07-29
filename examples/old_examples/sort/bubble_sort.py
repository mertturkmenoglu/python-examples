def bubble_sort(array, n):
    for i in range(n-1):
        for j in range(n-1-i):
            if array[j] > array[j + 1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array
