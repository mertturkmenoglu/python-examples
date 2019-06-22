# Example 033: File reading example
# Note: In Visual Studio Code with Python extension(intellisense), line 21 gives an error
# But it runs fine. I do not know what is the problem.

file = open("input.txt", mode = "r", encoding = "utf-8")

# Read first 10 data
print(file.read(8))
# Read more
print(file.read(6))

print("file.tell(): ", file.tell())
file.seek(0)

# Read all
print(file.read())

file.close()

# ------------- #
file = open("input.txt", mode = "r", encoding = "utf-8")
for line in file:
    print(line, end='')
print()
file.close