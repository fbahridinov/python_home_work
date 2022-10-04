# 1. Задайте список, состоящий из произвольных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётных позициях(не индексах).
# in
# 5
#
# out
# [10, 2, 3, 8, 9]
# 22

# Вариант № 1 без функции

import random

user_number = int(input('Arbitrary user number: '))

arb_numb = []
i = 0

while i < user_number:
    arb_numb.append(random.randint(0, 20))
    i += 1

print(arb_numb)

sum = 0
for position in arb_numb:
    if position % 2 == 0:
        sum += position
print(sum)

# Вариант № 2 тут с функции

import random

your_array = int(input('Arbitrary user number: '))

def list_create(number):
    list_numb = []
    for index in range(1, number + 1):
        list_numb.append(random.randint(0, 20))

    print(list_numb)
    amount = 0

    for position in list_numb:
        if list_numb.index(position) % 2 == 0:
            amount += position
    print(amount)

list_create(your_array)


# 2. Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# in
# 4
#
# out
# [2, 5, 8, 10]
# [20, 40]
#
# in
# 5
#
# out
# [2, 2, 4, 8, 8]
# [16, 16, 4]

import random

list_var = int(input('in: '))


def list_generator(value):
    gen_list = []
    for i in range(1, value + 1):
        gen_list.append(random.randint(0, 59))
    print(gen_list)

    gathering_list = []

    list_len = len(gen_list)

    for j in range(list_len // 2):
        gathering_list.append(gen_list[j] * gen_list[-1])

    if list_len % 2:
        gathering_list.append(gen_list[list_len // 2])

    print(gathering_list)


list_generator(list_var)


# 3. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Без использования встроенной функции преобразования, без строк.
# in
# 88
# out
# 1011000
#
# in
# 11
# out
# 1011


def compiler(value):
    if value <= 0:
        print(value)
    string_v = ""
    while value > 0:
        string_v = str(value % 2) + string_v
        value = value // 2

    print(string_v)


compiler(int(input('In: ')))

