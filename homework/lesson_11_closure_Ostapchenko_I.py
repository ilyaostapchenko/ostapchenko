""" Написал своими словами, чтоб было видно моё понимание о замыкание. """
print("""
Замыкание - это функция, которая передала ссылку на свой обьект другой
переменной вне зоны этой функции. Таким образом эта функция остаётся "живой"
после завершения работы функции в которую она вложена.
""")


def outer():
    """ Функция outer возращает обьект функции inner"""
    message = 'Hi teacher!'

    def inner():
        return message

    return inner


f = outer()
print(f())


def outer(message):
    """Returns a message with an argument"""
    def inner():
        
        return message

    return inner

hello_func = outer("Hello!")
bye_func = outer("Bye!")
print(hello_func(), bye_func(), sep="\n")


def make_quadratic(a, b, c):
    """Discriminant of the quadratic equation"""
    def quadratic(x):
        return a * x * x + b * x + c

    return quadratic


f1 = make_quadratic(3, 7, 2)
print(f1(2))

