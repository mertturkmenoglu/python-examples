def line_count(file_name):
    with open(file_name) as file:
        for i, l in enumerate(file):
            pass
    return i + 1

if __name__ == '__main__':
    print(line_count("file.txt"))