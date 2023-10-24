#!/usr/bin/python3
"""Define a Sqaure class"""


class Square:
	"""Define Sqaure"""

	def __init__(self, size=0):
		"""Initializes class Square"""
		self.__size = size
		if type(size) is not int:
			raise TypeError("size must be an integer")
		if size < 0:
			raise ValueError("size must be >= 0")

	def area(self):
		"""Define the area"""
		return self.__size * self.__size

	@property
	def size(self):
		""""Define getter method """
		return self.__size

	@size.setter
	def size(self, value):
		""""Define setter method"""
		self.__size = value
		if type(value) is not int:
			raise TypeError("size must be an integer")
		if value < 0:
			raise ValueError("size must be >= 0")

	def my_print(self):
		"""Define method 'my_print'the square with character #"""
		size = self.__size
		if size == 0:
			print()
		else:
			for i in range(0, size):
				print(size * "#")
