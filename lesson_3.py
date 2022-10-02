# 1. Задайте список, состоящий из произвольных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётных позициях(не индексах).
# in
# 5
#
# out
# [10, 2, 3, 8, 9]
# 22

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