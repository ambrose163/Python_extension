"""
Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление.
Функцию hex используйте для проверки своего результата.
"""

num_dec = int(input("Введите число: "))
res = ''
DIVIDER = 16

print(hex(num_dec))

while num_dec > 0:
    if num_dec % DIVIDER < 10:
        res = str(num_dec % DIVIDER) + res
    elif num_dec % DIVIDER == 10:
        res = 'A' + res
    elif num_dec % DIVIDER == 11:
        res = 'B' + res
    elif num_dec % DIVIDER == 12:
        res = 'C' + res
    elif num_dec % DIVIDER == 13:
        res = 'D' + res
    elif num_dec % DIVIDER == 14:
        res = 'E' + res
    elif num_dec % DIVIDER == 15:
        res = 'F' + res
    num_dec //= DIVIDER

print(res)