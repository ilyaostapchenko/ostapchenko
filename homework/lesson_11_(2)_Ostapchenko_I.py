''' map '''
print("""\"map\" принимает два аргумента - функцию и итератор. Применяется 
до каждого элемента итератора (будь это любым видом колекции) один раз
и возращает список результата.""")
"""Раньше мы делали так:"""
lst = ["1", "2", "3", "4", "5", "6", "7"]
new_lst = []
for item in lst:
    new_lst.append(int(item))
print("New list:", new_lst)

"""И тоже самое можно сделать, применив функию map()"""
old_lst = ["1", "2", "3", "4", "5", "6", "7"]
new_lst = list(map(int, old_lst))
print("New list:", new_lst)

"""пример на функции"""
def miles_to_kilometers(num_miles):
    return num_miles * 1.6

num_miles = [1, 3.4, 2.4, 9]
kilometers = list(map(miles_to_kilometers, num_miles))
print("Kilometers: ", kilometers)


""" lambda x: x ** 2 """
print("""\nЛямбда - анонимная функция, которая создаётся в одной строке и может быть передана другой функции.""")
""" встроенная функция "pow" """
def pow(x):
    return x * 2

print("Результат функции \"pow\":", pow(3))
""" lambda функция без переменной"""
print("На выходе \"lambda\" имеет тот же результат:", (lambda x: x * 2)(3)) # она не требует переменную.


""" filter """
print("""\nfilter() - это встроенная функция, которая принимает два параметра и возвращает объект-итератор.""")

a = ['python', 'c++', 'c++', True, 'python', 2, 'python']
def favorite_language(item):
    if type(item) == str:
        if item == 'python':
            return True
    if type(item) == int:
        return False
    else:
        return False

b = filter(favorite_language, a)

print("My favorite language is", list(b))# Также возращается один раз