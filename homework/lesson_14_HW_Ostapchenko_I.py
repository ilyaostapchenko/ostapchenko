"""The same tuples for all tasks"""
t = (1, 5, 8, 3)
tt = (2, 4, 7, 3)
ttt = (8, 4, 2, 3)
print(f"Tuple 1: {t}\nTuple 2: {tt}\nTuple 3: {ttt}")


"""Задание 1
Есть три кортежа целых чисел необходимо найти
элементы, которые есть во всех кортежах.
"""

def same_elements(t, tt, ttt):
    """ returns the same elements """
    same_numbers = []
    for i in tuple(t):
        if i in tt and i in ttt:
            if i not in same_numbers:
                same_numbers.append(i)
    return tuple(same_numbers)


print("\nTask 1:", same_elements(t, tt, ttt), sep='\n')


"""Задание 2
Есть три кортежа целых чисел необходимо найти
элементы, которые уникальны для каждого списка.
"""

def unique_elements(t, tt, ttt):
    """ Returns unique elements """
    unique_numbers = []
    for i in t:
        if i not in tt and i not in ttt:
            if i not in unique_numbers:
                unique_numbers.append(i)
    for j in tt:
        if j not in t and j not in ttt:
            if j not in unique_numbers:
                unique_numbers.append(j)
    for k in ttt:
        if k not in t and k not in tt:
            if k not in unique_numbers:
                unique_numbers.append(k)

    return tuple(unique_numbers)


print("\nTask 2:", unique_elements(t, tt, ttt), sep='\n')


"""Задание 3
Есть три кортежа целых чисел необходимо найти элементы, которые есть в каждом из кортежей и находятся
в каждом из кортежей на той же позиции.
"""
def same_index(t, tt, ttt):
    """Returns the same index of numbers with the same number"""
    for i in range(len(t)):
        for j in range(len(tt)):
            for k in range(len(ttt)):
                if t[i] == tt[j] == ttt[k] and i == j == k:
                    print(f"The index of number ({t[i]}) is {i}")

print("\nTask 3:")
same_index(t, tt, ttt)