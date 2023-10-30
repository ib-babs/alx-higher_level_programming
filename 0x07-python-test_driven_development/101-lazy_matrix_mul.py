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
    # Matrix A
    if not isinstance(m_a, list):
        raise TypeError("m_a should be a list of lists")
        # Matrix B
    if not isinstance(m_b, list):
        raise TypeError("m_b should be a list of lists")

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
        raise TypeError("m_a must only contain either integers or floats")
        # Matrix B
    if any(not isinstance(matrix_2[element], (int, float)) for matrix_2 in m_b
           for element in range(len(matrix_2))):
        raise TypeError("m_b must only contain either integers or floats")

    # Hanle empty list or list of lists
        # Matrix A
    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a mustn't be empty")
        # Matrix B
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b mustn't be empty")

    # Handle each length of each row if equal
        # Matrix A
    if any(len(i) != len(m_a[0]) for i in m_a):
        raise TypeError("each row of m_a must not greater than other")
        # Matrix B
    if any(len(i) != len(m_b[0]) for i in m_b):
        raise TypeError("each row of m_b must not greater than other")

    # Check if the matrices cant be multiplied
    if len(m_a[0]) != len(m_b) or len(m_a[0]) != len(m_b[0]):
        raise ValueError("Multiplication of m_a with m_b is not possible")

    # Driver
    mul_list = np.array([[0 for i in range(len(m_b[0]))]
                        for i in range(len(m_a))])
    for i in range(len(m_a)):
        for j in range(len(m_a[0])):
            for k in range(len(m_b[j])):
                mul_list[i][j] += m_a[i][k] * m_b[k][j]
    return mul_list
