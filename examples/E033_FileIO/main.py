# Example 033: File reading example
# Note: In Visual Studio Code with Python extension(intellisense), print() call with 
# named argument gives an error.
# But it runs fine. I do not know what is the problem.

# Open the file stream in classical way.
file = open("input.txt", mode = "r", encoding = "utf-8")

# Read first 8 data(bytes) and print it to stdout
print(file.read(8))

# Read more bytes
print(file.read(6))

# Where is the file indicator?
print("file.tell(): ", file.tell())

# Reset it
file.seek(0)

# Read all data in the file and print it to stdout
print(file.read())

# Close the file object
file.close()

# ------------- #
# Best way to read a file line by line.
file = open("input.txt", mode = "r", encoding = "utf-8")
for line in file:
    print(line, end='')

print()
file.close()