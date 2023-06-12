import glob
import os
from shutil import copy2
import sys


def get_files(path):
    '''Get all files in a folder'''
    files = glob.glob(f'{path}/*')
    return files


def getfullpath(path):
    '''Get full path of a file'''
    return os.path.abspath(path)


def copyfiles(src, dst):
    '''Copy files from src to dst'''
    if not os.path.isdir(dst):
        os.makedirs(dst)
    copy2(src, dst)


def split(data, count):
    '''Split data into count parts'''
    for i in range(1, len(data), count):
        if i + count - 1 > len(data):
            start, end = (i-1, len(data))
        else:
            start, end = (i-1, i+count-1)
        yield data[start:end]


def start_process(path, count):
    files = get_files(path)
    splited_data = split(files, count)

    for idx, folder in enumerate(splited_data):
        name = f'data_{idx}'
        for file in folder:
            copyfiles(getfullpath(file), getfullpath(name))


if __name__ == '__main__':
    """
        driver code
        To run this script
        python split_and_copy.py <input folder path> <20>
    """
    if len(sys.argv) != 3:
        print("Please provide correct parameters \
\npython split_and_copy.py <input folder path> <count>")
        sys.exit(0)

    if len(sys.argv) == 3:
        path = sys.argv[1]

        if os.path.isdir(path):
            count = int(sys.argv[2])
            start_process(path, count)
        else:
            print('Given directory does not exist')

    else:
        print("Please provide correct parameters")
