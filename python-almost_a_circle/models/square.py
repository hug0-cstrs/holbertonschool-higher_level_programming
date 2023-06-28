#!/usr/bin/python3
"""A module with a Square Class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """A Square class that inherits from Rectangle class"""
    def __init__(self, size, x=0, y=0, id=None):
        """A constructor method for the Square class

        Args:
            size (int): the size of the Square
            x (int): the x position of the Square
            y (int): the y position of the Square
            id (int): the identity of the new Square
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Return the print() and str() representation of a Square."""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x,
                                                 self.y, self.width)

    @property
    def size(self):
        """Get/set the size of the Square."""
        return self.width

    @size.setter
    def size(self, value):
        """ Setter size """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update the Square.

        Args:
            *args (ints): New attribute values.
                - 1st argument represents id attribute
                - 2nd argument represents size attribute
                - 3rd argument represent x attribute
                - 4th argument represents y attribute
            **kwargs (dict): New key/value pairs of attributes.
        """
        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                if a == 1:
                    self.size = arg
                elif a == 2:
                    self.x = arg
                elif a == 3:
                    self.y = arg
                a += 1

        elif kwargs and len(kwargs) != 0:
            for cle, value in kwargs.items():
                if cle == "id":
                    if value is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = value
                if cle == "size":
                    self.size = value
                elif cle == "x":
                    self.x = value
                elif cle == "y":
                    self.y = value
