#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return list(map(lambda x: [k ** 2 for k in x], matrix))
