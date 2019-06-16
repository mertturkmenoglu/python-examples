# Example 032: File output example

# 'w', 'a' or 'x' should be used

with open("output.txt",mode = 'w', encoding = 'utf-8') as file:
   file.write("FIRST LINE\n")
   file.write("SECOND LINE\n")
   file.write("THIRD AND THE LAST LINE\n")

# file stream is closed automatically