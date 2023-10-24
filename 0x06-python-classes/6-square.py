#!/usr/bin/python3
class Square:
    """Define Sqaure class that defines a square"""

    def __init__(self, size=0, position=(0, 0)):
        """Initializes class Square"""
        self.__size = size
        self.__position = position
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """Define 'area' method calculate the area of the square"""
        return self.__size * self.__size

    @property
    def size(self):
        """"The getter method 'size' gets the private instance '__size'"""
        return self.__size

    @size.setter
    def size(self, value):
        """"The setter method 'value' sets the private instance '__size'"""
        self.__size = value
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

    def my_print(self):
        """The method 'my_print' prints to stdout the square with character #"""
        size = self.__size
        pos = self.__position
        if size == 0:
            print()
        else:
            for i in range(0, size):
                if pos[1] > 1:
                    pass
                else:
                    print(pos[0] * " ", end='')
                print(size * "#")

    @property
    def position(self):
        """"The getter method 'position' gets the private instance '__position' """
        return self.__position

    @position.setter
    def position(self, value):
        """"The setter method 'value' sets the private instance '__position'"""
        if value[0] or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value
