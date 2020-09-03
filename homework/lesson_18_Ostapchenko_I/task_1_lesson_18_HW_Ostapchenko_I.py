def reader(text, mode='r'):
    """Opens file"""

    with open(text, mode) as file_obj:
        lines = file_obj.readlines()
    return lines


def compare_files(reader_1='', reader_2=''):
    """Returns unique strings"""

    uniq_strings = []
    lst_1 = [line.rstrip() for line in reader_1]
    lst_2 = [line.rstrip() for line in reader_2]
    for line in lst_1:
        if line not in lst_2:
            uniq_strings.append(line)
    for line_2 in lst_2:
        if line_2 not in lst_1:
            uniq_strings.append(line_2)
    return uniq_strings

def print_result(uniq_str):
    """Print unique lines"""
    for line in uniq_str:
        print(line)


if __name__ == '__main__':
    file = 'file_directory/file_1.txt'
    file_2 = 'file_directory/file_2.txt'

    uniq_str = compare_files(reader(file), reader(file_2))
    print_result(uniq_str)

