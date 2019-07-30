GLOBAL_VARIABLE = 42

if __name__ == "__main__":
    # Return the absolute value
    print(abs(20))
    print(abs(-20))
    print()

    # Return true if every item is true
    print(all([1, 2, 3]))
    print(all([1, False]))
    print()

    # Return binary representation
    print(bin(15))
    print(bin(2))
    print()

    # Return boolean representation
    print(bool(5))
    print(bool([]))
    print()

    # Return byte object
    print(bytes('emily', 'utf-8'))
    print(bytes([1, 2, 3]))
    print()

    # Returns true if the parameter is callable,
    var = 1
    print(callable(var))
    print(callable(lambda num: print(num)))
    print()

    # Takes source code and returns a code object
    # Code object can be executed by exec()
    string = 'name="emily"\nprint("Name:", name)'
    code = compile(string, 'print_name.py', 'exec')
    exec(code)
    print()

    # Sum of the iterable
    print(sum([1, 3, 5, 7]))
    print(sum([3, 5, 7], 2))
    print()

    # Return true if any item is true
    print(any([0, False, 1]))
    print(any([0, False]))
    print()

    # Returns a printable representation of an object and escapes the non-ASCII characters
    name = 'Emily'
    print(ascii(name))
    print()

    # noinspection SpellCheckingInspection
    bad_name = 'Møøse'
    print(ascii(bad_name))
    print('M\xf8\xf8se')
    print()

    # Returns a byte array object
    print(bytearray("emily you are the best", 'utf-8'))
    print()

    # Parse expression and run
    age = 17
    print(eval('age + 1'))
    print()

    # Parse floating number
    print(float("3.14"))
    print()

    # Return formatted representation
    print(format(42, "d"))
    print(format(3.14, "f"))
    print(format(15, "b"))
    print()

    # Return immutable frozenset object
    print(frozenset(('e', 'm', 'i', 'l', 'y', 'l', 'e', 'n', 'a')))
    print()

    # Returns the value of an attribute of an object.
    # If it is not found, returns the default value.
    class Person:
        name = "Emily"
        age = 35

    e = Person()
    print("Name: ", getattr(e, "name"))
    print("Name: ", e.name)

    try:
        print("Address: ", getattr(e, "address"))
    except AttributeError as ae:
        print(ae)
    print()

    # Returns the dictionary of the global symbol table
    print('Global var:',     globals()['GLOBAL_VARIABLE'])
    globals()['GLOBAL_VARIABLE'] = 3.14
    print('Global var:',     globals()['GLOBAL_VARIABLE'])
    print()

    # Returns true if an object has the given attribute
    class Car:
        model = "BMW"
        color = "BLACK"

    c = Car()
    print(hasattr(c, "model"))
    print(hasattr(c, "color"))
    print(hasattr(c, "year"))
    print()

    # Return an iterator from an iterable
    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    iterator = iter(numbers)
    print(next(iterator))
    print(next(iterator))
    print()

    # Return the length of an object
    print(len("Emily"))
    print(len([1, 2, 3, 4]))
    print()

    # Create a list
    print(list("Emily"))
    print(list())
    print()

    # Create a map object
    print(list(map(lambda num: num+1, [1, 2, 3])))
    print()

    # Get the character
    print(chr(65))
    print()

    # Get complex number
    print(complex(3, 4))
    print()

    # Delete an attribute from a class
    class Instrument:
        string_count = 6
        name = "Guitar"

    ins = Instrument()
    print(hasattr(ins, "name"))
    delattr(Instrument, "name")
    print(hasattr(ins, "name"))
    print()

    # Return a list of names in the local space
    x = 1
    print(dir(x))

    # Enumeration
    enum = enumerate([0, 1, 4, 9, 16, 25])
    print(list(enum))
