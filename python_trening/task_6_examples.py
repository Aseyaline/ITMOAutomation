# 1. Напишите функцию, которая:
# -принимает 1 аргумент
# -  a - значение по умолчанию (1, 2, 3, 4)
# - возвращает первый элемент этого кортежа


def func(a = (1, 2, 3, 4)):
    return a[0]
print(func())


# 2. Напишите функцию, которая:
# - принмамет 2 аргумента
# - radius
# - pi=3.14159
# - возвращет площадь круга (формула S = ПИ * r^2)


def func_2(radius, pi=3.14159):
    S = pi * radius ** 2
    return(S)
print(func_2(2))