#2. Для чисел в пределах от 20 до N найти числа, кратные 20 или 21. Use comprehension.

n = int(input('Введите число больше 20: '))
list = [i for i in range(20, n) if i % 20 == 0 or i % 21 == 0]
print("Список чисел кратных 20 или 21 в заданном диапазоне: ", list)