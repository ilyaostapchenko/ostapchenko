"""Формирую два списка заполняя их рандомными числами"""
from random import randint

amount = int(input("Amount of digits: "))
my_lst = []
my_lst2 = []
new_lst = []

for i in range(amount):
    i = randint(0, amount)
    my_lst.append(i)

for i in range(amount):
    i = randint(0, amount)
    my_lst2.append(i)

while True:
    answer = int(input("""
1 - Сформировать третий список, содержащий элементы обоих списков;
2 - Сформировать третий список, содержащий элементы обоих списков без повторений;
3 - Сформировать третий список, содержащий элементы общие для двух списков;
4 - Сформировать третий список, содержащий только уникальные элементы каждого из списков;
5 - Сформировать третий список, содержащий только минимальное и максимальное значение каждого из списков.
    ENTER YOUR ANSWER: """))

    # Формирую третий список, содержащий элементы обоих списков;
    if answer == 1:
        new_lst = my_lst + my_lst2
        break
    # Формирую третий список, содержащий элементы обоих списков без повторений;
    if answer == 2:
        for a, b in zip(my_lst, my_lst2):
            if a not in new_lst:
                new_lst.append(a)
            if b not in new_lst:
                new_lst.append(b)
        break
    # Формирую третий список, содержащий элементы общие для двух списков
    elif answer == 3:
        for i in my_lst:
            for j in my_lst2:
                if i == j:
                    new_lst.append(i)
        break

    # Формирую третий список, содержащий уникальные элементы каждого из списков;
    elif answer == 4:
        for i in my_lst:
            if i not in my_lst2 and i not in new_lst:
                new_lst.append(i)
        for i in my_lst2:
            if i not in my_lst and i not in new_lst:
                new_lst.append(i)
        break
    # Формирую третий список, содержащий только минимальное и максимальное значение каждого из списков.
    elif answer == 5:
        maximum = my_lst[0]
        minimum = my_lst[0]
        max2 = my_lst2[0]
        min2 = my_lst2[0]
        for i in range(len(my_lst)):
            if my_lst[i] > maximum:
                maximum = my_lst[i]
            if my_lst[i] < minimum:
                minimum = my_lst[i]
        for j in range(len(my_lst2)):
            if my_lst2[j] > max2:
                max2 = my_lst2[j]
            if my_lst2[j] < min2:
                min2 = my_lst2[j]
        lst = [maximum, minimum, max2, min2]
        for el in lst:
            new_lst.append(el)
        break # Или можно использовать функции min() max() вместо этого кода
# Вывод результатов:
if new_lst == []:
    print("1 List:", my_lst, "2 List:", my_lst2, sep='\n', end='')
else:
    print("1 List:", my_lst, "2 List:", my_lst2, "New list:", new_lst, sep='\n')
