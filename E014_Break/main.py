# Example 014: Break keyword example

students = ['Emily', 'Jonathan', 'Bruce', 'Anna', 'Su']

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
