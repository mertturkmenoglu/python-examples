# Example 007: Set data type example
# Unordered, unique item list

wrong_set = {1, 1}
first_set = {1, 2, 3, 4}
second_set = {3, 4, 5, 6}

print(wrong_set)
print(first_set)
print(second_set)

print(first_set.issuperset(wrong_set))
print(wrong_set.issubset(first_set))

print(first_set.intersection(second_set))
print(first_set.difference(second_set))
print(second_set.isdisjoint(wrong_set))

# Sets are unordered. It does not support indexing.
# You can't access an item via index number
# print(first_set[0]) will produce an error