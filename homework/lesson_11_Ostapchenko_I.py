""" GLOBAL """
x = 'Global function [ILYA]'


def foo():
    def bar():
        global x
        x = 'local'
        return x

    return bar()


""" ВКЛАДЕНА ФУНКЦІЯ """


def outer(arg):
    def inner(x):
        return x ** x

    if arg > 0:
        return inner(2)


""" local func """


def add_two(a):
    x = 2
    return a + x


# """ local namespace """
# def my_func(a, b):
#     global y
#     print(y)
#     y = 13
#
#
# if __name__ == '__main__':
#     y = 100
#     my_func(1,2)
#     print(y)
#     print(y)
#     print(y)


# def my_func_2(a, b):
#     global c
#     a, b = b, a
#     d = "Ilya"
#     print(a, b, c, d)
#
# a, b, c, d = 1, 2, "'c is global'", 4
# my_func_2(1, 2)
# print(a, b, c, d)

# """ Область nonlocal """


