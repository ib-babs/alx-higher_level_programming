#!/usr/bin/python3
"""
Class Module
"""


class BaseGeometry:
    """Define BaseGeometry class"""

    def area(self):
        """'area' function raises an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Integer Validator function"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
