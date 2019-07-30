if __name__ == "__main__":
    # Create a dictionary
    print(dict({"emily": 1, "diana": 2}))
    print()

    # Filter an iterable
    print(list(filter(lambda x: x > 0, [1, 2, -1, -2])))
    print()

    # Return the hash value
    print(hash(42))
    print(hash("emily"))
    print(hash(3.14))
    print(hash((1, 2, 3)))
    print()

    # Display help information about object
    help(print)
    print()

    # Get smallest element from a collection
    print(min(3, 5, 1, 10, 0))
    print(min([1, 0, 10, 5, 8, -1]))
    print()

    # Return a set
    print(set())
    print(set("emily"))
    print(set('emily is the best'))
    print()

    # Get hexadecimal representation of an integer
    print(hex(42))
    print(hex(-42))
    print()

    # Return a unique identity for the object
    one = 1
    print(id(1))
    print(id(one))
    print(id("emily"))
    print()

    # Set an attribute of an object
    class Car:
        model = "BMW"
        color = "BLACK"

    c = Car()

    # noinspection SpellCheckingInspection
    print("{} - {}".format(c.model, c.color))
    setattr(c, "model", "TOFAŞ")
    print("{} - {}".format(c.model, c.color))
    print()

    # Return sorted object
    print(sorted("emily"))
    print(sorted(["emily", "diana", "barbara", "el"], key=len, reverse=False))
    print()

    # Read from stdin
    inp = input("Enter value")
    print(inp)
    print()

    # Return an integer
    print(int('42'))
    print()

    # Return true if object is an instance of the class
    print(isinstance(42, int))
    print()

    # Return octal representation
    print(oct(18))
    print()

    # Return UNICODE value
    print(ord('A'))
    print(ord('Ü'))
    print()

    # Compute power
    print(pow(2, 3))
    print(pow(2, -1))
    print()

    # Return immutable sequence
    print(range(5, 20, 5))
    print()

    # Reverse items
    print(reversed([1, 2, 3, 4, 5]))
    print()

    # Round the numbers
    print(round(1.8))
    print(round(1.2))
    print(round(1.5))
    print()

    # Return true if class is subclass of the other one
    print(issubclass(int, float))
    print()

    # Convert to string
    print(str([1, 2, 3]))
    print()

    # Return a tuple
    print(tuple("emily"))
    print()

    # Return the type
    print(type(42))
    print(type("emily"))
    print()

    # Return __dict__ attribute
    vars(int)
    print()

    # Return a zip
    print(set(zip(["emily", "diana", "barbara"], [35, 42, 22])))
    print()
