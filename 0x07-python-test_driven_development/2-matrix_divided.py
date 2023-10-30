#!/usr/bin/python3
"""Matrix Divided function divide each element
in the list of the matix by the parameter `div`
in the function
Note that each list in the matix must be equal
Otherwise, exception is raised"""


def matrix_divided(matrix, div):
    """Define Matrix Division function
    Args:
        matrix and div"""
    for mtx in matrix:
        if any(not isinstance(m, (int, float)) for m in mtx):
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")
        if len(matrix[0]) != len(mtx):
            raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (float, int)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    return list(map(lambda x: [round(i / div, 2) for i in x], matrix))
