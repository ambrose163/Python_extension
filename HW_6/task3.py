"""
Создайте функцию генератор чисел Фибоначчи
"""

import itertools


def gen_fib():
    a, b = 1, 1
    while True:
        yield a
        a, b = b, a + b


print(list(itertools.islice(gen_fib(), 100)))