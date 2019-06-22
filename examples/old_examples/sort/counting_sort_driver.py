# Driver code for testing
# counting sort code
# Numers are arbitrary
# Can be changed

from random import randint
from counting_sort import counting_sort

n = randint(5, 20)

highest = 0

array = []

for i in range(n):
    tmp = randint(0, 100)

    if tmp > highest:
        highest = tmp

    array.append(tmp)

print(array)
print(counting_sort(array, highest))