# Example 010: Namespace example
import this

print(this.__doc__)

my_var = 5
print(id(5))
print(id(my_var))
my_second_var = 5
print(id(5))
print(id(my_var))
print(id(my_second_var))
