#!/usr/bin/python3


# Prints a matrix of integers.
def print_matrix_integer(matrix=[[]]):
    for j in matrix:
        idx = 0
        for i in j:
            print("{:d}".format(i), end='')
            idx < (len(j) - 1) and print(" ", end='')
            idx += 1
        print()
        idx = 0
