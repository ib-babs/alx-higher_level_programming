#!/usr/bin/python3
"""Author: Babatunde Ibrahim
print_square is a function that prints a '#' character
in multiple time of rows `size` paramter in the function
and in number of columns the parameter `size` is.
`size` must be integer, otherwise, error is raised"""


def print_square(size):
    """Define `print_square` function
    Arg(size):
        size: The length of the # to print"""

    if not isinstance(size, int) or (isinstance(size, float) and size < 0):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(0, size):
        print(size * "#")
