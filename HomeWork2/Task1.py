#1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
#in -> out
#- 6782 -> 23
#- 0.67 -> 13
#- 198.45 -> 27

a = float(input())
lenght_a = len(str(a))
a = int(a * 10 **(lenght_a - 2))
sum = 0

while (a > 0):
    sum = sum + (a % 10)
    a = a // 10
print (sum)
