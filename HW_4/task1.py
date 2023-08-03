"""
Напишите функцию для транспонирования матрицы
"""


def transpose_matrix(matrix):
    trans_m = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
    return trans_m


m = [[1, 2], [3, 4], [5, 6]]
print(transpose_matrix(m))