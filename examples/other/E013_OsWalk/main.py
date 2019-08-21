import os

if __name__ == '__main__':
    directory = input('Enter your start directory: ')

    for file in os.walk(directory):
        print('Dir: ', file[0])
        print('Subdirectories: ', file[1])
        print('Files: ', file[2])
        print('========')
