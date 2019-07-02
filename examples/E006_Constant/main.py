# Example 006: Constant variable
import constant

# Because of design principles, we do not have constanst in Python
# You may declare constant values in other languages via 'const' in C,
# 'val' in Kotlin, 'final' in Java... etc. But in Python, we do not have this
# We can declare variables(we call them variables but actually they do not change)
# in modules. We can call this module as constant, for example. So it is clearer that 
# the value in this module should not be changed

print(constant.PI)
print(constant.NAME)

# However, you can change it...
constant.PI = 1
print(constant.PI)