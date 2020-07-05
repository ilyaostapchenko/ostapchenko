"""
Задание 1
Напишите функцию, вычисляющую произведение
элементов списка целых. Список передаётся в качестве параметра.
Полученный результат возвращается из функции.
"""


def mult(lst):
    """Print integer multiplication"""
    numb = 1
    print(lst)
    for i in lst:
        numb *= i
    return numb


n = int(input("Enter end number: "))
lst = [i for i in range(1, n)]
display = mult(lst)

"""
Задание 2
Напишите функцию для нахождения минимума в
списке целых. Список передаётся в качестве параметра.
Полученный результат возвращается из функции.
"""


def minimum(lst):
    """return the minimum number"""
    return min(lst)


lst = [11, 2, 9, 13, 7]
show = lst

"""
Задание 3
Напишите функцию, определяющую количество простых чисел в списке целых. Список передаётся в качестве
параметра. Полученный результат возвращается из функции.
"""


def is_prime(lst):
    list_prime = []
    """Define compound numbers"""
    for i in lst:
        prime = True
        for j in range(2, i):
            if i % j == 0:
                prime = False
        """add prime numbers to list"""
        if prime:
            list_prime.append(i)
    return list_prime


n = int(input("End number: "))
print(is_prime(lst=[i for i in range(2, n)]))

"""
Задание 4
Напишите функцию, удаляющую из списка целых
некоторое заданное число. Из функции нужно вернуть
количество удаленных элементов.
"""

end_numb = int(input("Enter End Number: "))


def del_numbers():
    count = 0
    """Show the existing list"""
    print(lst)
    """Delete current item"""
    while True:
        n = int(input("Enter the number you want to delete, or type '0' to quit: "))
        for i in lst:
            if i == n:
                lst.remove(i)
                count += 1
        """ End the loop """
        if n == 0:
            return count


lst = [i for i in range(1, end_numb)]
print(f"The number of digits has been deleted: {del_numbers()}")

"""
Задание 5
Напишите функцию, которая получает два списка в
качестве параметра и возвращает список, содержащий
элементы обоих списков.
"""


def common_list(lst_1, lst_2):
    """join two lists together"""
    return lst_1 + lst_2


lst_1 = [i for i in range(1, 5)]
lst_2 = [j for j in range(5, 10)]
print(common_list(lst_1, lst_2))

"""
Задание 6
Напишите функцию, высчитывающую степень каждого
элемента списка целых. Значение для степени передаётся
в качестве параметра, список тоже передаётся в качестве
параметра. Функция возвращает новый список, содержа-
щий полученные результаты.
"""


def func(range_lst, n):
    """Add result to new list"""
    new_list = []
    for i in range_lst:
        new_list.append(i ** n)
    return new_list


n = int(input("Power: "))
range_lst = [i for i in range(2, 8)]
print(func(range_lst, n))
