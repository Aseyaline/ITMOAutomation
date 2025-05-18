# Определяем функцию
def add(x, y):
    return x + y


# Вызываем функцию
add(1, 2)

print(add(1, 2))
print(add('I a', 'm tester'))


def arg(a, b, c=2, d=3):
    return a+b+c+d


print(arg(1,1,1,1))
print(arg(2,2))
print(arg(1,1,1))


print(arg(2,2,0.3,1))

def str_arg(a,b,c,d):
    return a+b+c+d
print(str_arg('1','2','3','4'))
print(str_arg('1','2',d='4',c='3'))
