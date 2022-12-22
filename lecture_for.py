# Циклы

"""
# 1 for

for (переменная) in (итерируемый объект):
    твой код

"""

my_list = [1, 2, 6, 90, 45]
new_list = []

for num in my_list:
    new_num = num * 10 + 5
    new_list.append(new_num)


print(new_list)


"""
Специальные слова для управления циклом

continue - отправляет цикл на следующий круг
break - прерывание цикла

"""

my_list1 = [1, 2, 60, 90, 45]
new_list1 = []

for num1 in my_list1:
    new_num1 = num1 * 10 + 5

    if new_num1 == 905:
        break

    if new_num1 > 80:
        continue

    new_list1.append(new_num1)


print(new_list1)

"""
else в цикле for
    Выполняется код, если не встретился break

"""
print('===================')
my_list2 = [1, 2, 3, 20, 21, 22]

for num2 in my_list2:
    print(num2)
    if num2 == 20:
        break
else:
    print('break не встретился')


print('После for')



"""
Полезные структуры
for i in range(len(my_list)):  # получишь индексы элементов
    
"""
len_of_list = len(my_list)

print('range(len(my_list))')
for i in range(len(my_list)):
    print(i, my_list[i])

print('enumerate')
for index, value in enumerate(my_list):
    print(index, value)

save = len
len = print
print = len
range = print

len('Я печатаю через len')
len('Я опять печатаю через len')
range('Я опять печатаю через range')
