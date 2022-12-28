"""
Вызов функции происходит с помощью круглых скобок
def придумываешь_название_функции(аргументы, через, запятую):
    Код функции

"""
from math import sqrt

# Создание своей функции

print('start')


def my_great_func(arg1, arg2):
    print('=====================')
    print(arg1, arg2)
    print('sum', arg1 + arg2 + 9000)


print('До первого вызова')
my_great_func(10, 20)
my_great_func(12, 22)


# Аргументы по умолчанию
def my_great_func2(arg1, arg2=100):
    print('=====================')
    print(arg1, arg2)
    print('sum', arg1 + arg2 + 9000)


my_great_func2(10, 200)
my_great_func2(12)


# Работа с многими аргументами по умолчанию
def my_great_func3(arg1, arg2=0, arg3=0, arg4=0, arg5=0):
    print('=====================')
    print(arg1)
    print('sum', arg1 + arg2 + arg3 + arg4 + arg5)


my_great_func3(10, arg4=153)
my_great_func3(arg5=12, arg2=10, arg1=9)


def func_without_args():
    print('=====================')
    print('Просто')
    print('Печатаю')
    print('текст')


func_without_args()
func_without_args()
func_without_args()
func_without_args()

"""
Для чего писать функции:
1. Отдельный кусок логики
2. Переиспользование кода

"""

# Найти корни квадратного уравнения

"""
y = a * x ** 2 + b * x + c
"""

a = 2
b = 4
c = 2


# Вернуть значение из функции
def find_discr(a, b, c):
    d = b ** 2 - 4 * a * c
    return d


def find_roots(a, b, c):
    dis = find_discr(a, b, c)
    if dis > 0:
        x1 = (-b + sqrt(dis)) / (2 * a)
        x2 = (-b - sqrt(dis)) / (2 * a)
        return x1, x2
    elif dis == 0:
        x = -b / (2 * a)
        return x
    else:
        return 'Нет корней'


print(find_roots(a, b, c))
print(find_roots(10, 10, -10))
print(find_roots(10, 0, -10))
print(find_roots(12, 1, -10))
print(find_roots(12, 1, 10))

