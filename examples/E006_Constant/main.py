# Example 006: Constant variable
import constant

print(constant.PI)
print(constant.NAME)

# However, you can change it...
# We declare it in a module so it is more clear that
# the value should not be changed
constant.PI = 1
print(constant.PI)