# Example 013: While loop example

# Good old while loop, it works as you expected
# Do not forget to change loop variable somewhere inside
# your loop. And double check it.
i = 0
n = 5

while i < n:
    print(i)
    i += 1

i = 0
n = 3

# You can have else branch on while loop. Just like in for loop example
while i < n:
    print(i)
    i += 1
else:
    print('While loop is over')

print('After everything')
