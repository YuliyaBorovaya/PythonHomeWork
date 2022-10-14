#1. Вычислить число c заданной точностью d
#in
#Enter a real number: 9
#Enter the required accuracy '0.0001': 0.000001
#out
#9.000000

#in
#Enter a real number: 8.98785
#Enter the required accuracy '0.0001': 0.001
#out
#8.988

from decimal import Decimal

def round_number(number, d):
    number_round = Decimal(number)
    return number_round.quantize(Decimal(d))

print(round_number(input("Введите число: "),
      input("Введите требуемую точность: ")))


