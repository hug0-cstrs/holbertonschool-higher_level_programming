#!/usr/bin/python3
"""""A module with a simple class"""""


class Base:
    """This class will be the “base” of all other classes in this project.
    The goal of it is to manage id attribute in all your future classes and
    to avoid duplicating the same code (by extension, same bugs)
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        This is a constructor function that assigns an ID to an object either
        based on a given ID or by incrementing a counter.

        Args:
            id (int): The "id" parameter is an optional argument that can
            be passed to the constructor of an object. If a value is provided
            for "id", it will be assigned to the object's "id" attribute.
            If no value is provided for "id", a new value will be generated
            and assigned to.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
