# 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# in -> out
# - 6782 -> 23
# - 0.67 -> 13
# - 198.45 -> 27

number = input('Enter the number: ')
n = len(number) -1

number = float(number)

number = number * 10 ** n

summa = 0
while number > 0:
    summa += number % 10
    number = number // 10

print(summa)

# 2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# 1 - 1 * 1, 2 - 1 * 2, 3 - 1 * 2 * 3, 4 - 1 * 2 * 3 * 4 и т.д.
# - 4 -> [1, 2, 6, 24]
# - 6 -> [1, 2, 6, 24, 120, 720]


factorial = int(input('Enter number N: '))

result = 1
index = 1

while index < factorial:
    result *= index
    print(result)
    index += 1