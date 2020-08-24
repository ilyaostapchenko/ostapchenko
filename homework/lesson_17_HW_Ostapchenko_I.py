# """Задание 1
# Пользователь вводит с клавиатуры строку. Проверьте
# является ли введенная строка палиндромом. Палиндром — слово или текст, которое читается одинаково
# слева направо и справа налево. Например, кок; А роза
# упала на лапу Азора; доход; А буду я у дуба."""
def get_palindrome(text: str) -> str:
    """Returns text validation for palindrome"""
    for a, b in zip(text.lower().replace(" ", ''), reversed(text.lower().replace(" ", ''))):
        if a != b:
            return "No palindrome!"
    else:
        return f"This object \"{text}\" is palindrome!"


text = input("Enter palindrome: ")
print(get_palindrome(text))


# """
# Пользователь вводит с клавиатуры некоторый текст,
# после чего пользователь вводит список зарезервированных
# слов. Необходимо найти в тексте все зарезервированные
# слова и изменить их регистр на верхний. Вывести на
# экран измененный текст. """


def words(text: list, ) -> str:
    result = []
    reserved_words = ''
    while reserved_words != '0':
        reserved_words = input("Enter reserved words and 0 to complete the program: ").lower()
        result.append(reserved_words)

        for item, elem in enumerate(text):
            if elem in result:
                elem = elem.upper()
                text[item] = elem
    return ' '.join(text)


text = input("Enter text: ").replace(',', '').lower().split()
print(words(text=text))

# """Задание 3
# Есть некоторый текст. Посчитайте в этом тексте количество предложений и выведите на экран полученный
# результат.
# """
import re

def number_of_offer(text: str) -> str:
    signs = re.sub("[.?!]\s", '|', text)
    amount = len(signs.split('|'))
    return (f'There are {amount} sentences in this text.')


text = 'Привет! Меня зовут Илья и мне 25 лет. Я много искал себя в разных ' \
       'профессиях и все (по моему мнению) не так плохо получалось,' \
       ' но программирование получается гораздо сложнее и поэтому хочется его покорить.' \
       ' Как думаешь, верную тропинку я выбрал, или нет!? ' \
       ' Можно не отвечать, этот текст чтоб затестить программу.'
print(text)
print(number_of_offer(text=text))
