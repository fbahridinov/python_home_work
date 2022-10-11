# 1. Напишите программу, удаляющую из текста все слова, содержащие "абв". В тексте используется разделитель пробел.
# in
# Number of words: 10
#
# out
# авб абв бав абв вба бав вба абв абв абв
# авб бав вба бав вба
#
# in
# Number of words: 6
#
# out
# ваб вба абв ваб бва абв
# ваб вба ваб бва
#
# in
# Number of words: -1
#
# out
# The data is incorrect

from random import sample


def word_generator(a: int, b: str = 'абв'):
    array = []
    for i in range(a):
        c = sample(b, 3)
        array.append(''.join(c))
    return ' '.join(array)


d = word_generator(int(input()))
print(d)


def cleans_words(word: str) -> str:
    return word.replace(" абв", "")


print(cleans_words(d))
