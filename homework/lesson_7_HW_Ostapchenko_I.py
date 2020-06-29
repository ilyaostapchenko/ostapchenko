# """Задание 1
# Пользователь вводит с клавиатуры строку. Проверьте
# является ли введенная строка палиндромом. Палиндром — слово или текст, которое читается одинаково
# слева направо и справа налево. Например, кок; А роза
# упала на лапу Азора; доход; А буду я у дуба."""

p = input("Palindrome: ").lower().replace(' ', '')
l = len(p)
for i in range(l // 2):
    if p != p[::-1]:
        print("It's NOT palindrome!")
        break
else:
    print("It's palindrome!")


# """Задание 2
# Пользователь вводит с клавиатуры некоторый текст,
# после чего пользователь вводит список зарезервированных
# слов. Необходимо найти в тексте все зарезервированные
# слова и изменить их регистр на верхний. Вывести на
# экран измененный текст. """

text = input('Enter some text: ').replace(',', "").split()
result = []
res_words = ''
while res_words != "0":
    res_words = input("Tell me the reserved words and when end enter 0: ")
    result.append(res_words)

    for i, el in enumerate(text):
        if el in result:
            el = el.upper()
            text[i] = el

print(" ".join(text))


# """Задание 3
# Есть некоторый текст. Посчитайте в этом тексте ко-
# личество предложений и выведите на экран полученный
# результат."""

text = input('Some text: ').split()
signs = ['.', '!', '?']
sentences = 0
for i in text:
    for s in signs:
        if s in i:
            sentences += 1
print("Amount of sentences: ", sentences)