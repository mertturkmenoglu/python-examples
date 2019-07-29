from functools import partial


# Looks like a normal function definition
def function(arg1, arg2, arg3):
    return arg1 + arg2 + arg3


# Function assignment
# We leave the first parameter it will be 
# passed on actual function call
f = partial(function, 2, 3)

# Actual function call
# Expected output: 6
print(f(1))
