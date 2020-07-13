print("1. Написати функцію-декоратор, яка підносить до квадрату значення, "
      "що повертає функція, до якої декоратор застосовується.\n")


def decorator(*args):

    def squared(x):
        return x ** 2
    return squared



@decorator
def change_num(value):
    return value

if __name__ == '__main__':
    print("Number squared is:", change_num(4))
