#2. Напишите программу, которая найдёт произведение пар чисел списка.
#Парой считаем первый и последний элемент, второй и предпоследний и т.д.
#in
#4
#out
#[2, 5, 8, 10]
#[20, 40]
from random import sample

def find_multiple(number):
    if number > 0:
        numbers_list = sample(range(1, number*2), number)
        print(numbers_list)
        new_list = []
        for i in range(0, number//2):
            new_list.append(numbers_list[i]*numbers_list[number-1-i])
        if number % 2:
            new_list.append(numbers_list[number//2])
        print(new_list)
    
find_multiple(int(input()))