"""Задание 1
Напишите функцию, которая отображает на экран
форматированный текст, указанный ниже:
“Don't compare yourself with anyone in this world…
if you do so, you are insulting yourself.”
Bill Gates"""


def format_text():
    text = """Don't compare yourself with anyone in this world…
if you do so, you are insulting yourself."""
    name = "Bill Gates"

    print(f"{text}\n \t\t\t\t\t\t\t\t\t{name}")
    print("\n%s\n" % text + "\t" * 9 + "%s\n" % name)
    print("{}\n".format(text), "\t" * 9, "{}".format(name))


format_text()

"""Задание 2
Напишите функцию, которая принимает два числа
в качестве параметра и отображает все четные числа
между ними.
"""


def even_numbers(a, b):
    even_num = [i for i in range(a, b) if i % 2 == 0]
    print(even_num)


even_numbers(a=int(input("Enter first number: ")), b=int(input("Enter second number: ")))

"""Задание 3
Напишите функцию, которая отображает пустой или
заполненный квадрат из некоторого символа. Функция
принимает в качестве параметров: длину стороны квадрата, символ и переменную логического типа:
■ если она равна True, квадрат заполненный;
■ если False, квадрат пустой."""


def square(length, sign, active):
    while True:
        if active == "True":
            print(sign * length)
            for i in range(length - 2):
                print(sign + (" " * (length - 2)) + sign)
            print(sign * length)

        else:
            for i in range(length):
                for j in range(length):
                    print(sign, end="")
                print()

        break


square(length=int(input("Length: ")), sign=input("Sign: "), active=input("True / False???: "))

"""Задание 4
Напишите функцию, которая возвращает минимальное
из пяти чисел. Числа передаются в качестве параметров."""


def min_number(a, b, c, d, e):
    print(min(a, b, c, d, e))


min_number(7, 19, 36, 13, 3)

"""Задание 5
Напишите функцию, которая возвращает произведение чисел в указанном диапазоне. Границы диапазона
передаются в качестве параметров. Если границы диапазона перепутаны (например, 5 — верхняя граница, 25 —
нижняя граница), их нужно поменять местами."""


def range_of_numbers(a, b):
    n = 1
    """Меняю местами если верхняя граница меньше нижней"""
    if a < b:
        a, b = b, a
        """вывожу произвидение чисел на экран перебирая по одному"""
        for i in range(a, b, -1):
            n *= i
            print(n)
    else:
        for i in range(a, b, -1):
            n *= i
            print(n)


range_of_numbers(8, 6)

"""Задание 6
Напишите функцию, которая считает количество
цифр в числе. Число передаётся в качестве параметра. Из
функции нужно вернуть полученное количество цифр.
Например, если передали 3456, количество цифр будет 4.
"""


def amount_of_digits(x):
    print(len(str(x)))


amount_of_digits(43333)

""" Задание 7
Напишите функцию, которая проверяет является ли
число палиндромом. Число передаётся в качестве параметра. 
Если число палиндром нужно вернуть из функции
true, иначе false.
«Палиндром» — это число, у которого первая часть
цифр равна второй перевернутой части цифр. Например,
123321 — палиндром (первая часть 123, вторая 321, которая
после переворота становится 123), 546645 — палиндром,
а 421987 — не палиндром.  """


def palindrome(x):
    x = str(x)
    for a, b in zip(x, reversed(x)):
        if a != b:
            print("False")
            break
        else:
            print("True")
            break


palindrome(111)
