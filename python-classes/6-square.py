#!/usr/bin/python3
"""
This is the "Square"  module.

This module provides a simple Square class with initialize size.
"""


class Square:
    """A class that defines a square by size, which defaults 0.
    Also defines position using a tuple, which defaults (0, 0).
    Square can also get area, and print square using '#'.
    When printing, using position, offset on top and left.
    """
    def __init__(self, size=0, position=(0, 0)):
        """This is the __init__ method"""
        self.position = position
        self.size = size

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
           len(value) != 2 or type(value[0]) is not int or \
           type(value[1]) is not int or value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """This is a public instance method"""
        return self.__size * self.__size

    def my_print(self):
        """Print a square method"""
        if self.__size is 0:
            print("")
        else:
            if self.__position[1] is not 0:
                print("\n" * self.__position[1], end='')
            for i in range(self.__size):
                print(" " * self.__position[0], end='')
                print("#" * self.__size)
