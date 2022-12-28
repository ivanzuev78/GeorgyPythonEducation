# Логические операции

"""
Логическое И - and

10 > 5 - True
15 < 3 - False

a       b       a and b
True    True    True
False   True    False
True    False   False
False   False   False
"""

a = 10 > 5  # True
b = 15 < 3  # False
print('a', a)
print('b', b)

print('a and b', a and b)
# print(10 > 5 and 15 < 3)

"""
Логические ИЛИ - or

a       b       a or b
True    True    True
False   True    True
True    False   True
False   False   False


"""
print('=================================')
print('a or b', a or b)


"""
Логическое отрицание - not
not False -> True
not True -> False

"""
print('=================================')
print('not False', not False)
print('not True', not True)



"""
if (условие 1):  # обязательный блок
    Код выполняется, если (условие 1) True
elif (условие 2):  # необязательный блок
    Код выполняется, если (условие 1) False, а (условие 2) True
elif (условие 3):
    Код выполняется, если (условия 1 и 2) False, а (условие 3) True
elif (условие 4):
    Код выполняется, если (условия 1, 2 и 3) False, а (условие 4) True
else:  # необязательный блок
    Код выполняется, если все условия False

"""
print('=================================')
print('start')
num1 = -1000
num2 = 15

if num1 > num2:
    print('num1 > num2')

if num1 < num2:
    print('num1 > num2')

print('end')

print('b4 if')
if num1 > num2:
    print('1')
elif num1 + 3 > num2:
    print('2')
elif num1 + 100 > num2:
    print('3')
elif num1 + 200 > num2:
    print('4')
else:  # необязательный блок
    print('else')

print('after if')


print('===========================')

num1 = 10
num2 = 200

if num1 < num2 and num1 * 10 > num2:
    print('and 1')
elif num1 < num2 and num1 * 100 > num2:
    print('and 2')
elif num1 < num2 and num1 * 1000 > num2:
    print('and 3')
else:
    print('and 4')

print('after if')


print('===========================')

num1 = 10
num2 = 2

if num1 < num2 or num1 + num2 < 10:
    print('or 1')
elif num1 < num2 or num1 + num2 < 100:
    print('or 2')
elif (not num1 < num2) or num1 + num2 < 1000:
    print('or 3')
else:
    print('or 4')

print('after if')


"""
Операции сравнения
>      больше
<      Меньше
==     равно
>=     Больше или равно
<=     Меньше или равно
!=     Не равно

Результат сравнения это True или False
"""

print('==============')
item = {
    'color': 'blue',
    'shape': 'sphere'
}
if item['color'] == 'red' and item['shape'] == 'sphere':
    print('Это красный шар')
elif item['color'] == 'blue' and item['shape'] == 'sphere':
    print('Это синий шар')
elif item['color'] == 'red' or item['shape'] == 'sphere':
    print('Это красный предмет или сфера')
else:
    print('Не удалось распознать')

print('the end')
