#!/usr/bin/python3
"""
Class Module
"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    "Rectangle subclass"

    def __init__(self, size):
        """Initialization method"""
        super().__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """Area method"""
        return self.__size ** 2
