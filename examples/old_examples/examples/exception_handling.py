# Exception handling program

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

try:
    for i in range(len(numbers)):
        print(numbers[i])

    # Throws error
    print("11th element = %d" % (numbers[10]))

except IndexError:
    print("Index Error. Check your index!!!")
