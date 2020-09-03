def readlines(filename):
    with open(filename, "r") as file:
        lines = file.readlines()
        return lines


def get_longest_line(lines):
    lst = [item.strip() for item in lines]
    longest_line = lst
    for item in lst:
        if len(item) > len(longest_line):
            longest_line = item
    return len(longest_line)


if __name__ == '__main__':
    filename = "file_directory/testing_file.txt"
    lines = readlines(filename)
    print(f"Longest string length: {get_longest_line(lines)}")