#!/usr/bin/python3
class Square:
    """This is a class called 'Square'
     Sqaure is a class that defines a square
     """

    def __init__(self, size=0):
        """
        Initializes class Square with optional parameter 'size set to 0'
        """
        self.__size = size
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """
        The 'area' method calculate the area of the square
        """
        return self.__size * self.__size
