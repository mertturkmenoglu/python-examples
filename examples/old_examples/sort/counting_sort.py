def counting_sort(array, highest):
    ''' Counting sort algorithm implementation.
    For a given array and its highest number
    function returns a sorted array'''
    
    # This array will keep the existing numbers
    keep = [0 for i in range(highest + 1)]

    for var in array:
        keep[var] += 1
    
    sorted_array = []

    for i in range(len(keep)):
        # If a number exist, then add it to list
        if keep[i] > 0:
            for _ in range(keep[i]):
                sorted_array.append(i)

    return sorted_array