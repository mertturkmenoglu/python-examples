from os import listdir
from os.path import isfile, join

def get_file_list(path):
    return [file for file in listdir(path) if isfile(join(path, file))]

if __name__ == "__main__":
    user_path = input('Enter a path: ')
    print(get_file_list(user_path))