# Example 007: Set data type example
# Unordered, unique item list

# Every element must be unique. So in this set, there is only 1
wrong_set = {1, 1}

# Correct examples
first_set = {1, 2, 3, 4}
second_set = {3, 4, 5, 6}

# Print them to console
print(wrong_set)
print(first_set)
print(second_set)

# There are many set methods. You may know them from high school math.
print(first_set.issuperset(wrong_set))
print(wrong_set.issubset(first_set))

print(first_set.intersection(second_set))
print(first_set.difference(second_set))
print(second_set.isdisjoint(wrong_set))

# Sets are unordered. So indexing does not mean anything.
# It does not support indexing.
# You can't access an item via index number
# print(first_set[0]) will produce an error
# Any element can be anywhere
