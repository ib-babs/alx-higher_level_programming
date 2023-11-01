#!/usr/bin/python3
"""Author: Babatunde Ibrahim
`matrix_mul` is a function that multiplies two matrices
with two parameters: m_a - Matrix A, and m_b - Matrix B
Return: Multiplied matrix
Possible errors are handled"""


def matrix_mul(m_a, m_b):
    """Define Two Matrix Multiplication function
    Args(m_a, m_b):
    Matrix A and Matrix B"""

    # Handle list of list
    # Matrix A
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
        # Matrix B
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    # Handle the lists inside the list
        # Matrix A
    if any(not isinstance(matrix_1, list) for matrix_1 in m_a):
        raise TypeError("m_a must be a list of lists")
        # Matrix B
    if any(not isinstance(matrix_2, list) for matrix_2 in m_b):
        raise TypeError("m_b must be a list of lists")

    # Check the instance of element in the each list
        # Matrix A
    if any(not isinstance(matrix_1[element], (int, float)) for matrix_1 in m_a
           for element in range(len(matrix_1))):
        raise TypeError("m_a should contain only integers or floats")
        # Matrix B
    if any(not isinstance(matrix_2[element], (int, float)) for matrix_2 in m_b
           for element in range(len(matrix_2))):
        raise TypeError("m_b should contain only integers or floats")

    # Hanle empty list or list of lists
        # Matrix A
    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
        # Matrix B
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    # Handle each length of each row if equal
        # Matrix A
    if any(len(i) != len(m_a[0]) for i in m_a):
        raise TypeError("each row of m_a must be of the same size")
        # Matrix B
    if any(len(i) != len(m_b[0]) for i in m_b):
        raise TypeError("each row of m_b must be of the same size")

    # # Check if the matrices cant be multiplied
    # if len(m_a[0]) != len(m_b) or len(m_a[0]) != len(m_b[0]):
    #     raise ValueError("m_a and m_b can't be multiplied")

    # Driver
    mul_list = [[0 for i in range(len(m_b[0]))] for i in range(len(m_a))]
    for i in range(len(m_a)):
        for j in range(len(m_a[0])):
            for k in range(len(m_b[j])):
                mul_list[i][j] += m_a[i][k] * m_b[k][j]
    return mul_list
