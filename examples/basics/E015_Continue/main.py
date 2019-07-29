# Example 015: Continue keyword example

# It works as you expected
# Like break, it is considered as a bad programming habit.
# Do not use it unless you have to.

# Print only odd numbers in range
for i in range(0, 10):
    if i % 2 == 0:
        continue
    else:
        print(i)

print('After the loop')
