def reader(filename):
    '''Opens a file for reading'''

    with open(filename, "r") as f:
        string = f.read()
    return string


def writer(information, new_file):
    """Opens a file for writing"""
    with open(new_file, 'w') as f:
        content = f.write(information)
    return content


def get_count_of_symbols(string: str) -> int:
    """Returns the number of characters in a text file."""
    return len(string)


def get_number_of_lines(filename):
    """Returns the number of lines in a text file"""
    with open(filename, "r") as count_of_lines:
        string = count_of_lines.readlines()
        return len(string)


def get_number_of_vowels(string):
    """Returns the number of vowels in a text file."""
    tuple_of_vowels = ('a', 'e', 'i', 'o', 'u', 'y')
    vowels = 0
    for l in string:
        if l in tuple_of_vowels:
            vowels += 1
    return vowels


def get_count_of_consonants(string):
    """Returns the number of consonants in a text file"""
    tuple_of_consonants = ("b", "c", "d", "f", "g", "h", "j", "k", "l", "m",)
    tuple_of_consonants += ("n", "p", "q", "r", "s", "t", "w", "x", "z")
    consonants = 0
    for letter in string:
        if letter in tuple_of_consonants:
            consonants += 1
    return consonants


def get_number_of_digits(string):
    """Returns the number of digits in a text file"""
    numbers = 0
    for i in string:
        if i.isdigit():
            numbers += 1
    return numbers


def data_collection(filename):
    """Returns collection data from a text file"""
    string = reader(filename)
    symbols = (f"Count of symbols: {get_count_of_symbols(string)}")
    lines = (f"Number of lines: {get_number_of_lines(filename)}")
    vowels = (f"Number of vowels: {get_number_of_vowels(string)}")
    consonants = (f"Number of consonants: {get_count_of_consonants(string)}")
    digits = (f"Number of digits: {get_number_of_digits(string)}")
    return (symbols, lines, vowels, consonants, digits)


if __name__ == '__main__':
    filename = 'file_directory/testing_file.txt'
    new_file = 'file_directory/new_file.txt'
    collection = ("\n".join(data_collection(filename)))
    writer(collection, new_file)
    for item, line in enumerate(data_collection(filename), 1):
        print(f"{item}) {line}")
