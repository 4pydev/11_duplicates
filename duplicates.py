import sys
import os
from collections import namedtuple


def get_current_file(path):
    for root, directories, files in os.walk(path):
        for current_filename in files:
            current_file = File(root, current_filename)
            yield current_file


def is_files_equal(file1, file2):
    if file1.directory != file2.directory and \
       file1.name == file2.name and \
        os.path.getsize("{}/{}".format(file1.directory, file1.name)) == \
            os.path.getsize("{}/{}".format(file2.directory, file2.name)):
        return True
    return False


def add_to_matches(file1, file2, matches_dict):
    if file2.name not in founded_matches:
        founded_matches[file2.name] = set()
        founded_matches[file2.name].add(file1.directory)
        founded_matches[file2.name].add(file2.directory)
    else:
        founded_matches[file2.name].add(file2.directory)


def print_matches(matches_dict):
    if matches_dict != {}:
        for key in matches_dict.keys():
            print("File {} was founded in next directories:".format(key))
            for value in matches_dict.get(key):
                print("\t{}".format(value))
    else:
        print("Matches not found.")


if __name__ == '__main__':
    try:
        init_dir = sys.argv[1]
        founded_matches = {}
        File = namedtuple('File', 'directory name')
        for current_file in get_current_file(init_dir):
            for test_file in get_current_file(init_dir):
                add_to_matches(current_file, test_file, founded_matches) \
                    if is_files_equal(current_file, test_file) else False
        print_matches(founded_matches)
    except IndexError:
        print("Such directory doesn't exist.")
