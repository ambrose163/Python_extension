"""
Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
Программа должна возвращать сумму и произведение* дробей. Для проверки своего кода используйте модуль fractions.
"""

from fractions import Fraction

frac1 = input("Введите первую дробь: ")
frac2 = input("Введите вторую дробь: ")

numer1, denomin1 = map(int, frac1.split("/"))
numer2, denomin2 = map(int, frac2.split("/"))

f1 = Fraction(numer1, denomin1)
f2 = Fraction(numer2, denomin2)
print(f"\n*ПРОВЕРКА* Сумма дробей: {f1 + f2}, Произведение дробей: {f1 * f2} \n")

if denomin1 != denomin2:
    numer_sum = numer1 * denomin2 + numer2 * denomin1
    denomin_sum = denomin1 * denomin2
else:
    numer_sum = numer1 + numer2
    denomin_sum = denomin1

numer_prod = numer1 * numer2
denomin_prod = denomin1 * denomin2

print(f"Сумма дробей: {numer_sum}/{denomin_sum}")
print(f"Произведение дробей: {numer_prod}/{denomin_prod}")