#!/usr/bin/python3
"""
This is the "Square"  module.

This module provides a simple Square class with initialize size.
"""


class Square:
    """A class that defines a Square by size"""
    def __init__(self, size=0, position=(0, 0)):
        """This is the __init__ method"""
        self.position = position
        self.size = size

    def area(self):
        """This is a public instance method"""
        return self.__size * self.__size

    @property
    def size(self):
        """This is a public instance method"""
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

    @property
    def position(self):
        """This is a public instance method"""
        return self.__position

    @position.setter
    def position(self, value):
        """This is a public instance method"""
        if \
           type(value) is not tuple or \
           len(value) is not 2 or type(value[0]) is not int or \
           type(value[1]) is not int or value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def my_print(self):
        if self.__size == 0:
            print("")
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end='')
                print()
