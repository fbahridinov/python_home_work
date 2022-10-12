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

# 2. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.Входные и выходные
# данные хранятся в отдельных текстовых файлах.
# Алгоритм RLE
#
# in
# Enter the name of the file with the text:
# 'text_words.txt'
# Enter the file name to record:
# 'text_code_words.txt'
# Enter the name of the file to decode:
# 'text_code_words.txt'
#
# out
# aaaaavvvvvvvvvvvvvvvvvvvvvvvvvvvvvssssDDDdddFFggggOOiiiaa
# vvvvvvvvvvvbbwwPPuuuTTYyWWQQ
#
# out in file
# 'text_words.txt'
# aaaaavvvvvvvvvvvvvvvvvvvvvvvvvvvvvssssDDDdddFFggggOOiiiaa
# vbbwwPPuuuTTYyWWQQ
#
# 'text_code_words.txt'
# 5a29v4s3D3d2F4g2O3i2a1
# 1v2b2w2P3u2T1Y1y2W2Q
# ---------------------------------------------------------------------------------------------------------
# str_1 = input()
# s = ''
# for j in range(len(str_1)):
#     cnt = 0
#     for i in range(len(str_1)):
#         if str_1[0] == str_1[i]:
#             cnt += 1
#         else:
#             break
#     s += str_1[:1]
#     s += str(cnt)
#     str_1 = str_1[cnt:]
#     if len(str_1)<1:
#         break
# print(s)
#----------------------------------------------------------

def rle_encode(text="text_words.txt", code_text="text_code_words.txt"):
    if path.exists(text) and not path.exists(code_text):
        with open(text) as my_f_1, \
                open(code_text, "a") as my_f_2:
            for i in my_f_1:
                my_f_2.write("".join([f"{len(list(v))}{ch}" for ch, v in groupby(i)]))
    else:
        print("The files do not exist in the system!")

def rle_decode(text="out_text_words.txt", code_text="text_code_words.txt"):
    if path.exists(code_text):
        with open(code_text) as my_f_1, \
                open(text, "a") as my_f_2:
            for i in my_f_1:
                decode = ''
                count = ''
                for char in i:
                    if char.isdigit():
                        count += char
                    else:
                        decode += char * int(count)
                        count = ''
                my_f_2.write(decode)
    else:
        print("The files do not exist in the system!")
rle_encode()
rle_decode()