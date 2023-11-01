#!/usr/bin/python3
"""Rectangle is an class that defines a rectangle
Operations:
    Height and width of the rectangle
    Find the area of rectangle"""


class Rectangle:
    """Define Rectangle class"""
    number_of_instances = 0  # class attribute

    def __init__(self, width=0, height=0) -> None:
        """Initalize variable"""
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self) -> int:
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
    def height(self) -> int:
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

    def area(self):
        "Find the area of rectangle"
        return self.__width * self.__height

    def perimeter(self) -> int:
        """Find the perimeter of rectangle"""
        pmt: int = None
        if self.__width == 0 or self.__height == 0:
            pmt = 0
        else:
            pmt = (self.__width * 2) + (self.__height * 2)
        return pmt

    def __str__(self) -> str:
        """String representation of the class: Rectangle"""
        hash_chr = ''
        if self.__width == 0 or self.__height == 0:
            return ''
        for _ in range(self.__height):
            hash_chr += f"{self.__width * '#'}\n"
        return hash_chr[:-1]

    def __repr__(self) -> str:
        """Return string representation of object
        This can recreate a new instance with `eval` func"""
        return f"{type(self).__name__}({self.__width}, {self.__height})"

    def __del__(self):
        """Operation to perform when the class instance is deleted"""
        Rectangle.number_of_instances -= 1
        print("Bye Rectangle...")
