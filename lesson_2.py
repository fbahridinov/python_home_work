# 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# in -> out
# - 6782 -> 23
# - 0.67 -> 13
# - 198.45 -> 27

number = input('Enter the number: ')
n = len(number)

number = float(number)

number = number * 10 ** n

summa = 0
while number > 0:
    summa += number % 10
    number = number // 10

print(summa)