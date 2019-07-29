# Example 032: File output example

# 'w', 'a' or 'x' should be used
# We touch the topic on surface. Now let's see how do we handle basic io
# Operations like writing or reading file.
# We hve normal(text) mode and binary mode. Let's see the easy one: Text
# We use "with" keyword and open (create) a file stream. 
# Mode indicates that we will only write to this stream(it may be more complicated
# than this). File encoding is Unicode(utf-8 is the most common encoding).
# We call this object as "file".
# In "with" block, we call write method on file object. As you can guess, it writes
# given string to file. After this operations, Python will automatically call close
# method on the object and close the stream.
with open("output.txt", mode='w', encoding='utf-8') as file:
    file.write("FIRST LINE\n")
    file.write("SECOND LINE\n")
    file.write("THIRD AND THE LAST LINE\n")

# file stream is closed automatically
