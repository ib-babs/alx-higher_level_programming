#!/usr/bin/python3
"""
Class model - Rectangle
"""
from models.base import Base


class Rectangle(Base):
    """Define Rectangle class - Base subclass"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializing subclass constructor"""
        super().__init__(id)
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        if height <= 0:
            raise ValueError("height must be > 0")
        if x < 0:
            raise ValueError("x must be >= 0")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """Width getter"""
        return self.__width

    @width.setter
    def width(self, width):
        """Width setter"""
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """height getter"""
        return self.__height

    @height.setter
    def height(self, height):
        """height setter"""
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """x getter"""
        return self.__x

    @x.setter
    def x(self, x):
        """x setter"""
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """y getter"""
        return self.__y

    @y.setter
    def y(self, y):
        """y setter"""
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self) -> int:
        """Area method: width * height"""
        return self.__width * self.__height

    def display(self):
        """Prints in stdout, the character #"""
        for _ in range(self.__y):
            print()
        for _ in range(self.__height):
            print(self.__x * " ", end='')
            print(self.__width * "#")

    def __str__(self):
        """String representation of the subclass"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """Update the instance attribute"""
        try:
            if args and args != ():
                self.id = args[0]
                self.__width = args[1]
                self.__height = args[2]
                self.__x = args[3]
                self.__y = args[4]
            else:
                for key, val in kwargs.items():
                    if key == "y":
                        self.__y = val
                    if key == "x":
                        self.__x = val
                    if key == "width":
                        self.__width = val
                    if key == "height":
                        self.__height = val
                    if key == "id":
                        self.id = val
        except:
            pass

    def to_dictionary(self):
        """Return dictionary representation of Rectangle"""
        return {"x": self.__x, "y": self.__y,
                "id": self.id, "height": self.__height,
                "width": self.__width}
