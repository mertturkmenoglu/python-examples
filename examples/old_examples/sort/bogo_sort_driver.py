from random import randint
from bogo_sort import bogo_sort

n = randint(5, 10)

array = []

for i in range(n):
    array.append(randint(0, 100))

print(array)
print(bogo_sort(array))
