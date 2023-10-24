#!/usr/bin/python3
class Square:
    """Define Sqaure class"""

    def __init__(self, size=0):
        """Initializes class Square"""
        self.__size = size
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
