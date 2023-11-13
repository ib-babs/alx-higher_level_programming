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
        try:
            if args and args != ():
                self.id = args[0]
                self.size = args[1]
                self.x = args[2]
                self.y = args[3]
            else:
                for key, val in kwargs.items():
                    if key == "y":
                        self.y = val
                    if key == "x":
                        self.x = val
                    if key == "id":
                        self.id = val
                    if key == "size":
                        self.size = val
        except:
            pass

    def to_dictionary(self):
        """Return dictionary representation of Square"""
        return {"id": self.id, "x": self.x,
                "size": self.size, "y": self.y}
