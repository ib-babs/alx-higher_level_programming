#!/usr/bin/python3
"""Rectangle is an class that defines a rectangle
Operations:
    Height and width of the rectangle
    Find the area of rectangle"""


class Rectangle:
    """Define Rectangle class"""

    def __init__(self, width=0, height=0) -> None:
        """Initalize variable"""
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Getting width property"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setting width property"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getting height property"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setting height property"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
