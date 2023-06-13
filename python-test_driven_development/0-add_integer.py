#!/usr/bin/python3
"""
This module is composed by a function that adds two numbers
"""


def add_integer(a, b=98):
    """This function adds two integers
    Args: two integers
    Return: integer"""
    if (type(a) is int or type(a) is float):
        if (type(b) is int or type(b) is float):
            return int(a) + int(b)
        else:
            raise TypeError("b must be an integer")
    else:
        raise TypeError("a must be an integer")
