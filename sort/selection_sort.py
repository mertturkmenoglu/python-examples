def selection_sort(array, n):
    for i in range(n-1):
        location = i
        min = array[i]
        for j in range(i+1, n):
            if(array[j] < min):
                min = array[j]
                location = j
        array[location] = array[i]
        array[i] = min
    return array
