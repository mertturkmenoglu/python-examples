# Example 010: Namespace example
import this

# Zen of Python
print(this.__doc__)

# Python's memory approach is kinda different, if you are coming from
# C or Java or similar language base. Here, python chooses a memory location
# and writes the value 5 to that memory. Than, my_var becomes an alias for this
# memory. It is an etiquette. It is a reference(but not like in C or Java).
# You can see that both of the outputs are the same. We are printing memory locations
my_var = 5
print(id(5))
print(id(my_var))

# Now add another alias
my_second_var = 5
print(id(5))
print(id(my_var))
print(id(my_second_var))
