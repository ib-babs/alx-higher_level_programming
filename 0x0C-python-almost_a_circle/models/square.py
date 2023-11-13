#!/usr/bin/python3
"""
Class model - Rectangle
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Rectangle subclass"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialization of Rectangle subclass"""
        super().__init__(id=id, x=x, y=y, width=size, height=size)
        self.__size = size

    def __str__(self):
        """String representation of the subclass"""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """size getter method"""
        return self.__size

    @size.setter
    def size(self, value):
        """size setter method"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update the instance attributes"""
        if args and args != ():
            i = 0
            listme = ["id", "size", "x", "y"]
            for arg in args:
                setattr(self, listme[i], arg)
                i += 1
        else:
            for key, val in kwargs.items():
                setattr(self, key, val)

    def to_dictionary(self):
        """Return dictionary representation of Square"""
        return {"id": self.id, "x": self.x,
                "size": self.size, "y": self.y}
