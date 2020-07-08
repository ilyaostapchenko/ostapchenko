""" Написал своими словами, чтоб было видно моё понимание о замыкание. """
print("""
Замыкание - это функция, которая передала ссылку на свой обьект другой
переменной вне зоны этой функции. Таким образом эта функция остаётся "живой"
после завершения работы функции в которую она вложена.
""")


def outer():
    """ Функция inner возращает обьект функции inner"""
    message = 'Hi teacher!'

    def inner():
        """ Функция inner выводит переменную message функции outer"""
        print(message)

    return inner


""" переменнуй f присваиваем результат функции outer """
f = outer()
""" Переменная f указывает на обьект функции inner в которой находится переменна message."""
print(f())


def outer(message):
    """ функция outer содержит в себе вложеную функцию inner """

    def inner():
        """ в которой есть ссылка на обьект переменной message. Inner принтует message """
        print(message)
    """ Outer возращает ссылку на обьект функции inner """
    return inner

""" И тут делаю замыкание. Создаю переменные и связываю их с обьектом функции inner через функцию outer """
hello_func = outer("Hello!")
bye_func = outer("Bye!")
""" Принтую результат работы программы """
print(hello_func(), bye_func(), sep="\n")



""" Аналогичный код к Вашему приммеру """
def make_quadratic(a, b, c):
    """ discriminant of the quadratic equation' """
    def quadratic(x):
        return a * x * x + b * x + c

    return quadratic


f1 = make_quadratic(3, 7, 2)
print(f1(2))

