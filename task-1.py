from random import randint
import numpy as np


class Matrix:
    max_num = 0

    def __init__(self, matrix: list):
        self.matrix = matrix

    def __str__(self):
        if len(self.matrix) <= 0:
            return ''

        self.max_num = np.max(self.matrix)
        len_chars = len(self.get_matrix_row(self.matrix[0])) - 1
        top_border = '-' * len_chars + '\n'
        matrix = ''

        for lst in self.matrix:
            matrix += self.get_matrix_row(lst) + top_border

        return top_border + matrix

    def __add__(self, other):
        matrix = []
        self_matrix = self.matrix
        other_matrix = other.matrix
        len_self = len(self_matrix)
        len_other = len(other_matrix)
        i = 0

        if len_self < len_other:
            self_matrix, other_matrix = other_matrix, self_matrix

        max_len_matrix = len_self if len_self > len_other else len_other

        while i < max_len_matrix:
            if i < len_self and i < len_other:
                list_1 = self_matrix[i]
                list_2 = other_matrix[i]
                len_1 = len(list_1)
                len_2 = len(list_2)

                if len_1 < len_2:
                    list_1, list_2 = list_2, list_1
                    len_1, len_2 = len_2, len_1

                matrix.append([list_1[j] + list_2[j] if j < len_1 and j < len_2 else list_1[j] for j in range(len_1)])
            else:
                old_matrix = self_matrix[i][:]

                if len(self_matrix[0]) < len(other_matrix[0]):
                    old_matrix.append(0)

                matrix.append(old_matrix)

            i += 1

        return Matrix(matrix)

    def get_matrix_row(self, lst):
        return ''.join(['| ' + (' ' * (len(str(self.max_num)) - len(str(i)))) + str(i) + ' ' for i in lst]) + '|\n'


my_matrix_1 = Matrix([[randint(0, 100) for _ in range(2)] for _i in range(2)])
my_matrix_2 = Matrix([[randint(0, 100) for _ in range(2)] for _j in range(2)])
my_matrix_3 = Matrix([[randint(0, 100) for _ in range(2)] for _k in range(2)])
my_matrix_4 = my_matrix_2 + my_matrix_1 + my_matrix_3
print(my_matrix_1)
print(my_matrix_2)
print(my_matrix_3)
print(my_matrix_4)
