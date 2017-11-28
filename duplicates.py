import sys
import os


def get_current_file(path):
    for root, directories, files in os.walk(path):
        for current_file in files:
            yield "{}/{}".format(root, current_file)


def get_test_file(path):
    for root, directories, files in os.walk(path):
        for test_file in files:
            yield "{}/{}".format(root, test_file)


def is_files_equal(file1, file2):
    if file1 != file2:
        if os.path.basename(file1) == os.path.basename(file2) and \
                        os.path.getsize(file1) == os.path.getsize(file2):
            return True
    return False


if __name__ == '__main__':
    try:
        init_dir = sys.argv[1]
        print("Initial directory:", init_dir, '\n')
#        for current_file in get_current_file(init_dir):
#            path, filename = current_file
#            print('{path}/{filename}'.format(path=path,
#                                             filename=filename))

        for current_file in get_current_file(init_dir):
            for test_file in get_test_file(init_dir):
                if is_files_equal(current_file, test_file):
                    print("Match found:\n\t{}\n\t{}\n".format(current_file,
                                                          test_file))


    except IndexError:
        print("Such directory doesn't exist.")
