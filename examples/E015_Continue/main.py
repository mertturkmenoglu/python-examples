# Example 015: Continue keyword example

# Print only odd numbers in range
for i in range(0, 10):
    if i % 2 == 0:
        continue
    else:
        print(i)

print('After the loop')
