# 3. Задайте последовательность чисел. Напишите программу, которая выведет 
# список неповторяющихся элементов исходной последовательности в том же порядке.

import random

n = int(input("Введите длину списка: "))
rand_list=[]
for i in range(n):
    rand_list.append(random.randint(1,9))
print(rand_list)

found = set()
found_again = set()

for a in rand_list:
    if a in found_again:
        continue
    if a in found:
        found.remove(a)
        found_again.add(a)
    else:
        found.add(a)

print(list(found))
