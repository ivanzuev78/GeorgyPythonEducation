# while


"""
while (условие):
    Код, который будет выполняться по кругу, пока (условие) True

"""

i = 0

while i < 5:
    print('Старт одного круга')
    print(i)
    i = i + 1
    print('Конец одного круга')

print('Цикл окончен')


"""
Специальные слова для управления циклом

continue - отправляет цикл на следующий круг
break - прерывание цикла

"""


i = 0

while i < 5:
    print('Старт одного круга')
    print(i)
    i = i + 1
    if i == 4:
        break

    if i == 3:
        continue

    print('Конец одного круга')

print('Цикл окончен')


"""

else в цикле while
    Выполняется код, если не встретился break

аналогично for
"""
print('догонялки ========================')
a = 20
b = 1
while a > b:
    if a + b > 50:
        print('Игра провалилась')
        break
    a += 1  # a = a + 1
    b *= 2
    print(a, b)

else:
    print('Игра прошла успешно')
