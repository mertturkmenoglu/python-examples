def next_char(ch):
    if 'A' <= ch < 'Z' or 'a' <= ch < 'z':
        return chr(ord(ch) + 1)
    elif ch == 'Z':
        return 'A'
    elif ch == 'z':
        return 'a'
    else:
        # Whitespace, newline or other unicode chars
        return ch


if __name__ == '__main__':
    i_file = input('Input file path: ')
    o_file = input('Output file path: ')

    with open(i_file, mode="r", encoding="utf-8") as file:
        with open(o_file, mode="w", encoding="utf-8") as out:
            for line in file:
                for c in line:
                    out.write(next_char(c))
