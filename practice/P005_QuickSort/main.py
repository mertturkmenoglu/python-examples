# Practice 005: Quick sort implementation

def quickSort(array: list, begin: int = 0, end: int = 0):
    if begin < end:
        pIndex = partititon(array, begin, end)
        quickSort(array, begin, pIndex - 1)
        quickSort(array, pIndex + 1, end)


def partititon(array: list, begin: int, end: int):
    pivot = array[end]
    i = begin - 1

    for j in range(begin, end):
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]

    i += 1
    array[i], array[end] = array[end], array[i]

    return i

if __name__ == "__main__":
    import random
    
    n = random.randint(7, 15)
    arr = []
    for i in range(n):
        arr.append(random.randint(-n, n))
    
    print(arr)
    quickSort(arr, begin=0, end=len(arr) - 1)
    print(arr)
