#!/usr/bin/python3
"""
Class Module
"""
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """Define 'Rectangle' class"""

    def __init__(self, width, height):
        """Initialization method"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Area method"""
        return self.__width * self.__height

    def __str__(self):
        """Return rectangle description"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
