def decorator(fun):
    def print_info(*args):
        print("Before executing function")
        fun(args[0])
        print("After executing function")
    return print_info


@decorator
def my_print(e):
    print("Printing element: ", e)


if __name__ == '__main__':
    my_print('Emily')
