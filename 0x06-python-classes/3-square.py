#!/usr/bin/python3
"""Define a Sqaure class"""


class Square:
    """Define a Sqaure"""

    def __init__(self, size=0):
        """Initializes class"""
        self.__size = size
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """The 'area' method calculate the area of the square"""
        return self.__size * self.__size
