# Створити множини: A, B, C з довільними елементами.
# Знайти:
# 1. Різні елементи для A, B
# 2. Однакові елементи для A, C
# 3. Об'єднання всіх трьох множин.

A = {1, 4, 8, 3, 5, 9}
B = {1, 6, 7, 3, 0}
C = {1, 4, 2, 3, 8, 7}

D = A.intersection(C)
E = A.symmetric_difference(B)
F = A.union(B, C)

print("1. Різні елементи для A, B", A ^ B)
print("1. Різні елементи для A, B", E)


print("2. Однакові елементи для A, C", A & C)
print("2. Однакові елементи для A, C", D)

print("3. Об'єднання всіх трьох множин.", A | B | C)
print("3. Об'єднання всіх трьох множин.", F)