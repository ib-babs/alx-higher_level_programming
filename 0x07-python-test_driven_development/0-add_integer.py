#!/usr/bin/python3
"""Functioin that Add 2 integer
Args(a, b):
    a: first integer
    b: second integer
return: Sum of ` a` and `b`"""


def add_integer(a, b=98):
    """
    Define Add function
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    return a + b
