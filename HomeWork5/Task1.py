# 1. Напишите программу, удаляющую из текста все слова, содержащие "абв". В тексте используется разделитель пробел.
# in
# Number of words: 10
# out
# авб абв бав абв вба бав вба абв абв абв
# авб бав вба бав вба
# in
# Number of words: 6
# out
# ваб вба абв ваб бва абв
# ваб вба ваб бва

import random

txt = input('Какое слово нужно удалить? ')
num_w = (int(input('Сколько составить слов: ')))
list_w = []
print('Tекст: ')
for i in range(num_w):
    random_txt = random.sample(txt, 3)
    list_w.append("".join(random_txt))

print(" ".join(list_w))

print("Полученный текст: ")
list_w2 = list(filter(lambda x: txt not in x, list_w))
print(" ".join(list_w2))