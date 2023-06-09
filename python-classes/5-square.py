#!/usr/bin/python3
"""
This is the "Square"  module.

This module provides a simple Square class with initialize size.
"""


class Square:
    """A class that defines a Square by size"""
    def __init__(self, size=0):
        """This is the __init__ method"""

        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """This is a public instance method"""
        return self.__size * self.__size

    def my_print(self):
        if self.__size == 0:
            print("")
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end='')
                print()

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        self.value = value

        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
