# Example 036: Exception handling example

# Base class
class Error(Exception):
    pass

class EvenNumberException(Error):
    pass

class BigNumberException(Error):
    pass


for i in range(10):
    print("Number: ", i)

    try:
        if i % 2 == 0:
            raise EvenNumberException
        elif i > 7:
            raise BigNumberException
    except EvenNumberException:
        print("Exception: Value is an even number")
    except BigNumberException:
        print("Exception: Number is greater than the limit")

print("After the loop")

