"""
Напишите функцию, которая принимает на вход строку —
абсолютный путь до файла. Функция возвращает кортеж из трёх
элементов: путь, имя файла, расширение файла.
"""

import os


def elems_path(my_path):
    return os.path.split(my_path)[0], *os.path.split(my_path)[-1].split('.')


print(elems_path('C:\GeekBrains\Python_next\home_work\Python_eхtension\HW_5\htask1.py'))