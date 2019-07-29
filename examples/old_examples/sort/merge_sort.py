def merge_sort(array, start, end):
    if start < end:
        mid = (start + end) // 2
        merge_sort(array, start, mid)
        merge_sort(array, mid + 1, end)
        merge(array, start, mid, end)


def merge(array, start, mid, end):
    tmp = []

    ia = start
    ib = mid + 1

    while ia <= mid and ib <= end:
        if array[ia] <= array[ib]:
            tmp.append(array[ia])
        else:
            tmp.append(array[ib])

    while ia <= mid:
        tmp.append(array[ia])

    while ib <= end:
        tmp.append(array[ib])

    for i in range(start, end + 1):
        array[i] = tmp[i - start]
