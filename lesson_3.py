# 1. Задайте список, состоящий из произвольных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётных позициях(не индексах).
# in
# 5
#
# out
# [10, 2, 3, 8, 9]
# 22

# Вариант № 1

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

# Вариант № 2

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

