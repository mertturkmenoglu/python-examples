# Example 031: File input output example
# Opening a file

try:
    file = open('input.txt', "r")
    print('File opened')
finally:
    print('Calling close() method')
    file.close()

print('Now another way(with)')

with open("input.txt", encoding = 'utf-8', mode = "r+") as file:
    print('File opened. No need for close() method')
