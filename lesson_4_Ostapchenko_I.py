"""Завдання 1
Користувач вводить 3 числа. Далі в залежності від вибору користувача потрібно знайти суму або добуток цих чисел.
(Тобто програма запитує в користувача, що потрібно зробити)
"""
print("Write me three numbers, and I will refund you the sum or multiplication of these numbers.")
a = input("a: ")
b = input("b: ")
c = input("c: ")

operation = input('What to do with them? ("+", "*"): ')
if "+" in operation:
    sum = int(a) + int(b) + int(c)
    print("Sum: " + str(sum))
else:
    mult = int(a) * int(b) * int(c)
    print("Multiplication: " + str(mult))


# """
# Завдання 2
# Користувач вводить 3 числа. Далі в залежності від вибору користувача потрібно знайти найбільше з 3-х,
# найменше, або середнє арифметичне.
# (Подібно до 1-го)
# """
# print("Write me three numbers, and I will find the largest of the 3 numbers,"
#       + " the smallest or arithmetic mean.")
# a = int(input("a: "))
# b = int(input("b: "))
# c = int(input("c: "))
# operation = input("What number to find? (largest, smallest, or arithmetic mean): ")
# if "min" in operation:
#     m = a
#     if m > b:
#         m = b
#     if m > c:
#         m = c
#     print('min: ' + str(m))
#     # print(min(a, b, c))
# elif "max" in operation:
#     if a > b > c:
#         print("max: ", str(a))
#     elif b > a > c:
#         print("max: ", str(b))
#     else:
#         print("max: ", str(c))
#     # m = a
#     # if m < b:
#     #     m = b
#     # if m < c:
#     #     m = c
#     # print("max: ", str(m))
#     # print(max(a, b, c))
# else:
#     list = [a, b, c]
#     print("arithmetic mean: " + str(sum(list) / len(list)) )


# """
# Завдання 3
# Користувач вводить з клавіатури кількість метрів. В залежності від вибору -
# програма конвертує їх в сантиметри, міліметри, або кілометри.
# """

# m = int(input("Enter the number of meters or kilometers: "))
# operation = input("Convert them to centimeters, millimeters or kilometers?: ")

# if "mm" in operation:
#     if m == 1:
#         meter = "meter"
#     else:
#         meter = "meters"
#     mm = m / 0.001
#     print(str(m) + " " + meter + " equal to " + str(mm) + " millimeters.")
# elif "cm" in operation:
#     if m == 1:
#         meter = "meter"
#     else:
#         meter = "meters"
#     cm = m / 0.01
#     print(str(m) + " " + meter + " equal to " + str(cm) + " centimeters.")
# elif "km" in operation:
#     if m == 1:
#         meter = "meter"
#     else:
#         meter = "meters"
#     km = m / 1000
#     print(str(m) + " " + meter + " equal to " + str(km) + " kilometers.")


