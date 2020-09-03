def reader(filename):
    """Opens a file for reading."""
    with open(filename, "r+") as readline:
        lines = readline.readlines()
    return lines


def writer(new_file, new_text):
    """Opens a file for writing."""
    with open(new_file, "w") as new_f:
        new_f.write(new_text)
    return new_file


def set_string(lines):
    """Delete a last string."""
    if lines:
        del (lines[-1])
    return lines


if __name__ == '__main__':
    filename = "file_directory/file_2.txt"
    new_file = 'file_directory/file_3.txt'
    lines = reader(filename)
    set_string(lines)
    new_text = ("".join(lines))
    writer(new_file, new_text)
    
