#!/usr/bin/python3
"""A module with a Rectangle Class"""
from models.base import Base


class Rectangle(Base):
    """A Rectangle class that inherits from Base class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """A constructor method for the Rectangle class

        Args:
            width (int): the width of the Rectangle
            height (int): the height of the Rectangle
            x (int): the x position of the Recangle
            y (int): the y position of the Rectangle
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Gets the height of the Rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the height of the Rectangle"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Gets the height of the Rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height of the Rectangle"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        """Gets the height of the Rectangle"""
        return self.__x

    @x.setter
    def x(self, value):
        """Sets the height of the Rectangle"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        """Gets the height of the Rectangle"""
        return self.__y

    @y.setter
    def y(self, value):
        """Sets the height of the Rectangle"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        """Public method that returns the area value
        of the Rectangle instance
        """
        return self.width * self.height

    def display(self):
        """ displays a rectangle """
        rectangle = self.y * "\n"
        for i in range(self.height):
            rectangle += (" " * self.x)
            rectangle += ("#" * self.width) + "\n"
        print(rectangle, end='')

    def __str__(self) -> str:
        """
        __str__ method
        """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.__x, self.__y,
                                                       self.__width,
                                                       self.__height)

    def update(self, *args, **kwargs):
        """Update the Rectangle.

        Args:
            *args (ints): New attribute values.
                - 1st argument represents id attribute
                - 2nd argument represents width attribute
                - 3rd argument represent height attribute
                - 4th argument represents x attribute
                - 5th argument represents y attribute
            **kwargs (dict): New key/value pairs of attributes.
        """
        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.width = arg
                elif a == 2:
                    self.height = arg
                elif a == 3:
                    self.x = arg
                elif a == 4:
                    self.y = arg
                a += 1

        elif kwargs and len(kwargs) != 0:
            for cle, value in kwargs.items():
                if cle == "id":
                    if value is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = value
                elif cle == "width":
                    self.width = value
                elif cle == "height":
                    self.height = value
                elif cle == "x":
                    self.x = value
                elif cle == "y":
                    self.y = value
