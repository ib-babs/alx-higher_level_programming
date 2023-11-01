#!/usr/bin/python3
"""Author: Babatunde Ibrahim
`lazy_matrix_mul` is a function that multiplies two matrices
with two parameters: m_a - Matrix A, and m_b - Matrix B
Return: Multiplied matrix
Possible errors are handled"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Define Lazy Two Matrix Multiplication function
    Args(m_a, m_b):
    Matrix A and Matrix B"""

    # Handle list of list
    # Matrix A and B
    if not isinstance(m_a, list) or not isinstance(m_b, list):
        raise TypeError("Scalar operands are not allowed, use '*' instead")

    # Handle the lists inside the list
        # Matrix A
    if any(not isinstance(matrix_1, list) for matrix_1 in m_a):
        raise TypeError("m_a have to be a list")
        # Matrix B
    if any(not isinstance(matrix_2, list) for matrix_2 in m_b):
        raise TypeError("m_b have to be a list")

    # Check the instance of element in the each list
        # Matrix A
    if any(not isinstance(matrix_1[element], (int, float)) for matrix_1 in m_a
           for element in range(len(matrix_1))):
        raise TypeError("invalid data type for einsum")
        # Matrix B
    if any(not isinstance(matrix_2[element], (int, float)) for matrix_2 in m_b
           for element in range(len(matrix_2))):
        raise TypeError("invalid data type for einsum")

    # Hanle empty list or list of lists
        # Matrix A
    if m_a == [] or m_a == [[]]:
        raise ValueError(
            "shapes (1,0) and (2,2) not aligned: 0 (dim 1) != 2 (dim 0)")
        # Matrix B
    if m_b == [] or m_b == [[]]:
        raise ValueError(
            "shapes (2,2) and (1,0) not aligned: 2 (dim 1) != 1 (dim 0)")

    # Handle each length of each row if equal
        # Matrix A
    if any(len(i) != len(m_a[0]) for i in m_a):
        raise TypeError("setting an array element with a sequence.")
        # Matrix B
    if any(len(i) != len(m_b[0]) for i in m_b):
        raise TypeError("setting an array element with a sequence.")

    # Check if the matrices cant be multiplied
    if len(m_a[0]) != len(m_b) or len(m_a[0]) != len(m_b[0]):
        raise ValueError(
            "shapes (2,3) and (2,2) not aligned: 3 (dim 1) != 2 (dim 0)")

    # Driver
    mul_list = np.array([[0 for i in range(len(m_b[0]))]
                        for i in range(len(m_a))])
    for i in range(len(m_a)):
        for j in range(len(m_a[0])):
            for k in range(len(m_b[j])):
                mul_list[i][j] += m_a[i][k] * m_b[k][j]
    return mul_list
