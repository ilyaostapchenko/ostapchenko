# The same tuples for all tasks
t1 = (1, 4, 8, 3)
t2 = (1, 6, 7, 3)
t3 = (1, 4, 2, 3)
print(f"Tuple 1: {t1}\nTuple 2: {t2}\nTuple 3: {t3}")

# Задание 1
# Есть три кортежа целых чисел необходимо найти
# элементы, которые есть во всех кортежах.



def same_elements(t1, t2, t3):
    """ returns the same elements """
    same_numbers = []
    for i in tuple(t1):
        if i in t2 and i in t3:
            if i not in same_numbers:
                same_numbers.append(i)
    return tuple(same_numbers)


print("\nTask 1:", same_elements(t1, t2, t3), sep='\n')

# Задание 2
# Есть три кортежа целых чисел необходимо найти
# элементы, которые уникальны для каждого списка.



def unique_elements(t1, t2, t3):
    """ Returns unique elements """
    unique_numbers = []
    for i, j, k in zip(t1, t2, t3):
        if i not in t2 and i not in t3:
            if i not in unique_numbers:
                unique_numbers.append(i)

        if j not in t1 and j not in t3:
            if j not in unique_numbers:
                unique_numbers.append(j)

        if k not in t1 and k not in t2:
            if k not in unique_numbers:
                unique_numbers.append(k)

    return tuple(unique_numbers)


print("\nTask 2:", unique_elements(t1, t2, t3), sep='\n')


# Задание 3
# Есть три кортежа целых чисел необходимо найти элементы, которые есть в каждом из кортежей и находятся
# в каждом из кортежей на той же позиции.


def same_index(t1, t2, t3):
    """Returns the same index of numbers with the same number"""
    for i in range(len(t1)):
        if t1[i] == t2[i] == t3[i] and i == i == i:
            print(f"The index of number ({t1[i]}) is {i}")


print("\nTask 3:")
same_index(t1, t2, t3)