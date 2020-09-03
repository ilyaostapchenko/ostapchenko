def decorator(func):
    """Returns additional function for reading or writing"""
    def wrapper(filename, mode):
        global file
        with open(filename, mode) as file:
            action = func(filename)
        return action
    return wrapper


@decorator
def reader(text):
    """Returns a file for reading"""
    content = file.read()
    return content


@decorator
def writer(way):
    """Returns a file to writing"""
    file.write(change_)
    return way


def change_text(content):
    """Returns modified text to a file"""
    if old_word in content:
        change_content = content.replace(old_word, new_word)
        return change_content
    else:
        return f"{old_word}"


if __name__ == '__main__':
    filename = "file_directory/file_2.txt"
    old_word = input("Enter word: ")
    new_word = input("Enter new word: ")
    content = reader(filename, 'r')
    change_ = change_text(content)
    writer(filename, "w")
    print(change_)
