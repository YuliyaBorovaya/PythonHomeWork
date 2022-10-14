#. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
#Без использования встроенной функции преобразования, без строк.

def convert_to_2(number):
    if number > 0:
        my_list = []
        while number > 0:
            my_list.insert(0, number % 2)
            number = number//2
        print(''.join(map(str, my_list)))  
    else:
        print("Ошибка!")

convert_to_2(int(input()))