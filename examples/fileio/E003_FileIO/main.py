# Example 031: File input output example
# Opening a file

# Opening file like it is in Java. We have a try catch block, in try, we have
# a file object. If it opens successfully, then everything is fine.
# If there is a problem(file not found, for example. Or maybe incorrect access), 
# it should continue from the catch block. Whatever happens, final action is closing
# the file stream. Normally, Python should handle all the things but we do not want to
# occupy sources for too long. So it is best to close the stream and give the resources
# back. After finally block, program continues normally.
try:
    file = open('input.txt', "r")
    print('File opened')
except FileNotFoundError:
    print("Error")
finally:
    print('Calling close() method')
    file.close()

print('Now another way(with)')

# The recommended way to handle file operations. You should use the with keyword. 
# It handles streams automatically. You do not need to call close method on file object
# because "with" will call it for you.
with open("input.txt", encoding='utf-8', mode="r+") as file:
    print('File opened. No need for close() method')
