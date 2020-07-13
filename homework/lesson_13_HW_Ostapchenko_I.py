print("""Реалізувати такі сортування:
1. Сортування бульбашкою
2. Швидке сортування
""")


def bubble_sort(num):
    """ Bubble sort """

    swapped = True
    while swapped:
        swapped = False
        for i in range(len(num) - 1):
                if num[i] > num[i + 1]:
                    num[i], num[i + 1] = num[i + 1], num[i]
                    swapped = True


num = [5, 3, 8, 7, 1]
print(f"Old list: {num}")
bubble_sort(num)
print(f"Sorted list by bubble sort: {num}")


def quickSort(lst):
    """ Quick Sort """
    if len(lst) < 2:
        return lst
    pivot = lst[0]
    less = [i for i in lst[1:] if i <= pivot]
    greater = [i for i in lst[1:] if i > pivot]
    return quickSort(less) + [pivot] + quickSort(greater)


lst = [15, 10, 33, 3]
print(f"\nOld list: {lst}")
print(f"Sorted list by quick sort: {quickSort(lst)}")