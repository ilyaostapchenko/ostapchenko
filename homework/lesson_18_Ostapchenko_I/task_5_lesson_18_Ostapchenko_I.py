def reader(filename):
    with open(filename, 'r') as file_obj:
        content = file_obj.read()
    return content


def get_count_word(content):
    number_word = content.count(word)
    return number_word



if __name__ == '__main__':
    filename = "file_directory/file_2.txt"
    word = input("Enter word: ")
    content = reader(filename)
    if word not in content:
        print(f"Word \"{word}\" is missing from \"{filename}\"")
    print(f"Number of word {word} is {get_count_word(content)}.")
