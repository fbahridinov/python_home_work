# 1. Вычислить число c заданной точностью d
# in
# Enter a real number: 9
# Enter the required accuracy '0.0001': 0.000001
#
# out
# 9.000000
#
# in
# Enter a real number: 8.98785
# Enter the required accuracy '0.0001': 0.001
#
# out
# 8.988

from decimal import Decimal

real_number = Decimal(input('Enter a real number: '))

req_accuracy = input('Enter the required accuracy 0.0001: ')

number = real_number.quantize(Decimal(req_accuracy))
print(number)

# 2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# Простые делители числа
#
# in
# 54
#
# out
# [2, 3, 3, 3]
#
# in
# 9990
#
# out
# [2, 3, 3, 3, 5, 37]
#
# in
# 650
#
# out
# [2, 5, 5, 13]


def numeral(value):
    l = []
    prime_number = 2
    while prime_number <= value:
        if value % prime_number == 0:
            l.append(prime_number)
            value //= prime_number
            prime_number = 2
        else:
            prime_number += 1
    print(l)


numeral(int(input('in: ')))
