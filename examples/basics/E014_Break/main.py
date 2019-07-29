# Example 014: Break keyword example

# You have break keyword in other languages. They are considered
# as a bad programming habit. Do not use them if you really have to.
# But in Python, sometimes it makes your life easier.

# Lets have a list
students = ['Emily', 'Jonathan', 'Bruce', 'Anna', 'Su']

# Iterate over the list "UNTIL" you find the Bruce.
# When you find the Bruce, "BREAK" the loop and continue
for student in students:
    if student == 'Bruce':
        print('I found the Bruce')
        break
    else:
        print('{} is not Bruce'.format(student))

i = 0
n = 5

while i < n:
    print(i)
    if i == 3:
        print('Break the loop')
        break
    i += 1

i = 0
n = 10
# A bad example to use break.
# Just use for loop.
while True:
    if i == n:
        break
    else:
        print(i)
        i += 1
