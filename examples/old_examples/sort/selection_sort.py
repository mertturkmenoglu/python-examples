def selection_sort(array, n):
    for i in range(n-1):
        location = i
        min_element = array[i]
        for j in range(i+1, n):
            if array[j] < min_element:
                min_element = array[j]
                location = j
        array[location] = array[i]
        array[i] = min_element
    return array
