"""Returns a compact view"""
import pprint

def show_result(*args) -> None:
    """Returns result"""
    for item in args:
        pprint.pprint(item, width=1)
        input("Press to continue...")


def add_new_word(english_word: str, french_word: str) -> dict:
    """Returns a new word in the dictionary"""
    dictionary = {
        'English word': english_word,
        'French word': french_word,
    }
    VOCABULARY.append(dictionary)
    return dictionary


def remove_word(dict_word: str) -> dict:
    """Removes the selected dictionary from the list"""
    del_word = {}
    for index, word in enumerate(VOCABULARY):
        if word["English word"] == dict_word:
            del_word.update(word)
            del VOCABULARY[index]
            return del_word
        if word['French word'] == dict_word:
            del_word.update(word)
            del VOCABULARY[index]
            return del_word


def list_dictionary(vocabulary: list) -> list:
    """Returns a list of dictionaries"""
    return vocabulary


def find_word(word: str) -> dict:
    """Returns a dictionary from the list"""
    for key in VOCABULARY:
        if key["English word"] == word:
            return key
        if key["French word"] == word:
            return key
    return f"Word {word} doesn't exist."


def update_word(word: str, new_word: str) -> list:
    """Returns a list of dictionary updates"""
    for key in VOCABULARY:
        if key["English word"] == word:
            key["English word"] = new_word
            return VOCABULARY
        if key["French word"] == word:
            key["French word"] = new_word
            return VOCABULARY


if __name__ == '__main__':
    ADD_WORD = 'add'
    DEL_WORD = "del"
    SEARCH_WORD = "find"
    UPDATE_WORD = "update"
    SHOW_LIST = 'list'
    EXIT = "quit"
    VOCABULARY = [{"English word": "cat", "French word": "chatte"}, {"English word": "apple", "French word": "pomme"}]
    while True:
        print(f"""Choices:
    ADD NEW WORD -> {ADD_WORD}
    DEL WORD -> {DEL_WORD}
    SEARCH WORD -> {SEARCH_WORD}
    UPDATE WORD -> {UPDATE_WORD}
    SHOW LIST -> {SHOW_LIST}
    CLOSE DICTIONARY -> {EXIT}
        """)
        choice = input("MAKE YOUR CHOICE: ")
        if choice == EXIT:
            print("Bye Bye!", end='')
            break
        elif choice == ADD_WORD:
            vocabulary = add_new_word(
                english_word=input("English word: "),
                french_word=input("French word: ")
            )
            show_result(vocabulary)
        elif choice == DEL_WORD:
            delete_word = remove_word(
                dict_word=input("Enter word that you want to remove: ")
            )
            show_result(delete_word)
        elif choice == SEARCH_WORD:
            search_word = find_word(
                word=input("Enter the word you want to find: ")
            )
            show_result(search_word)
        elif choice == UPDATE_WORD:
            new_word = update_word(
                word=input("What a word you want update?: "),
                new_word=input("New word: ")
            )
            show_result(new_word)
        elif choice == SHOW_LIST:
            show_result(list_dictionary(VOCABULARY))