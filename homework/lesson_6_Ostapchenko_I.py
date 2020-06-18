# """Задание 1
# Пользователь вводит с клавиатуры два числа (начало и конец диапазона). Требуется проанализировать все
# числа в этом диапазоне по следующему правилу: если
# число кратно 7, его надо выводить на экран."""
#
# def multiples():
#
#     a = int(input("Start number: "))
#     b = int(input("End number: "))
#     for i in range(a, b):
#         if i % 7 == 0:
#             print(f"Multiple of 7 equals {i}")
#
# multiples()


# """Задание 2
# Пользователь вводит с клавиатуры два числа (начало и конец диапазона). Требуется проанализировать все
# числа в этом диапазоне. Нужно вывести на экран:
# 1. Все числа диапазона;
# 2. Все числа диапазона в убывающем порядке;
# 3. Все числа, кратные 7;
# 4. Количество чисел, кратных 5."""
#
#
# class Numbers():
#     def __init__(self):
#         self.first_number = int(input("Start number: "))
#         self.end_number = int(input("End number: "))
#
#     def all_range_numbers(self):
#         print("\nAll range numbers:")
#         for i in range(self.first_number, self.end_number):
#             print(i)
#
#     def all_reverse_range_numbers(self):
#         print("\nAll reverse range numbers:")
#         for i in reversed(range(self.first_number, self.end_number)):
#             print(i)
#
#     def multiples(self):
#         print("All numbers that are multiples of 7:")
#         for i in range(self.first_number, self.end_number):
#             if i % 7 == 0:
#                 print(i)
#
#     def len_mult_num(self):
#         amount = []
#         print("Amount of numbers that are multiples of 5:")
#         for i in range(self.first_number, self.end_number):
#             if i % 5 == 0:
#                 amount.append(i)
#         print(len(amount))
#
#
# digits = Numbers()
# # digits.all_range_numbers()
# # digits.all_reverse_range_numbers()
# # digits.multiples()
# digits.len_mult_num()

# """Задание 3
# Пользователь вводит с клавиатуры два числа (начало
# и конец диапазона). Требуется проанализировать все числа
# в этом диапазоне. Вывод на экран должен проходить по
# правилам, указанным ниже.
# Если число кратно 3 (делится на 3 без остатка) нужно
# вывести слово Fizz. Если число кратно 5 нужно вывести слово Buzz.
# Если число кратно 3 и 5 нужно вывести
# Fizz Buzz. Если число не кратно не 3 и 5 нужно вывести
# само число"""
#
#
# def multiples():
#     a = int(input("Start number: "))
#     b = int(input("End number: "))
#
#     print("\nAll numbers that are multiples of 3:")
#     for i in range(a, b):
#         if i % 3 == 0:
#             print("Fizz")
#
#     print("\nAll numbers that are multiples of 5:")
#     for i in range(a, b):
#         if i % 5 == 0:
#             print("Buzz")
#
#     print("\nAll numbers multiple of 3 and 5:")
#     for i in range(a, b):
#         if (i % 3 == 0) and (i % 5 == 0):
#             print("Fizz Buzz")
#
#     print("\nAll numbers are not a multiple of 3 and 5:")
#     for i in range(a, b):
#         if (i % 3 != 0) and (i % 5 != 0):
#             print(i)
#
#
# multiples()
