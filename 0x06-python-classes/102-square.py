#!/usr/bin/python3
"""Define a Sqaure class"""


class Square:
    """Define Sqaure class"""

    def __init__(self, size=0):
        """Initializes class"""
        self.__size = size
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """Define area"""
        return self.__size * self.__size

    @property
    def size(self):
        """"Define getter method"""
        return self.__size

    @size.setter
    def size(self, value):
        """"The setter method"""
        self.__size = value
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

    def __lt__(self, other):
        """Define less than method"""
        return self.__size ** 2 < other.__size ** 2

    def __le__(self, other):
        """Define less than equalto method"""
        return self.__size ** 2 <= other.__size ** 2

    def __gt__(self, other):
        """Define greater than method"""
        return self.__size > other.__size

    def __ge__(self, other):
        """Define greater than equalto method"""
        return self.__size ** 2 >= other.__size ** 2

    def __eq__(self, other):
        """Define equalto method"""
        return self.__size ** 2 == other.__size ** 2

    def __ne__(self, other):
        """Define not equalto than method"""
        return self.__size ** 2 != other.__size ** 2
