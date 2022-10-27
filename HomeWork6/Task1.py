#1. Представлен список чисел. Необходимо вывести элементы исходного списка, 
#значения которых больше предыдущего элемента. Use comprehension.

res_list = []
list = [int(i) for i in input('Введите числа через пробел: ').split()]
for i in range(1, len(list)):
    if list[i] > list[i-1]:
        (res_list.append(list[i]))
print('Введенный список: ', list)
print('Результат: ', res_list)