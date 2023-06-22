#!/usr/bin/python3
"""A module with a class BaseGeometry"""


class BaseGeometry:
    """A class with a no implemented method"""
    def area(self):
        """A public instance method that raises an Exception

        Args: nothing
        Returns: nothing
        Raises: Exception
        """
        raise Exception("area() is not implemented")
