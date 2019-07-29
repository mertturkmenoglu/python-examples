# Practice 005: Quick sort implementation


def quick_sort(array: list, begin: int = 0, end: int = 0):
    if begin < end:
        p_index = partition(array, begin, end)
        quick_sort(array, begin, p_index - 1)
        quick_sort(array, p_index + 1, end)


def partition(array: list, begin: int, end: int):
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
    for k in range(n):
        arr.append(random.randint(-n, n))
    
    print(arr)
    quick_sort(arr, begin=0, end=len(arr) - 1)
    print(arr)
