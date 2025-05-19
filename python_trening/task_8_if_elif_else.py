# Программа проверяет является число положительным
# или отрицательным и выводит соответствующее сообщение


num = 3
# num = -5
# num = 0


if num >= 0:
    print('Число больше либо равно 0')
else:
    print('Число отрицательное')


# str_2 содержит в себе str_1?
# str_1 = 'test'
# str_2 = 'test1'

def yes_or_no(str_1, str_2):
    if str_1 in str_2:
        return 'yes'
    else:
        return 'no'
print(yes_or_no('test', 'test1'))


# num_float = 3.4
# num_float = 0
num_float = -4.5


if num_float > 0:
    print('Положительное число')
elif num_float == 0:
    print('Ноль')
else:
    print('Отрицательное число')


permit_print = True

if num > 0 and permit_print:
    print('num - положительное число')
elif not permit_print:
    print('Печать запрещена')


# Задача
# Напишите программу, которая отвечает какое ваше текущее звание исходя из курса
# варианты званий:
# - бакалавр - 1-4 (включительно)
# - магистр - 5-6 (включительно)
# - аспирант - 7-9 (включительно)
# Если введенное число не соответствует ни одному диапазону, выводите на печать:
# "Введите корректный год обучения"


def func_course(i: int) -> str:
    if i >= 1 and i <= 4:
        print('Бакалавр')
    elif i > 4 and i <= 6:
        print('Магистр')
    elif i > 6 and i <= 9:
        print('Аспирант')
    else:
        print('Введите корректный год обучения')

func_course(6)


# Задача
# Дано число. Если оно больше 100 или меньше -100, то вывести на экран символ "-"
# Иначе вывести на экран символ "+"


a = 235
def func_number(n: int):
    if n > 100 or n < -100:
        print('-')
    else:
        print('+')

func_number(a)