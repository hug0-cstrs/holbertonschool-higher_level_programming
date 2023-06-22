#!/usr/bin/python3
"""A module with a function that check if
the object is exactly an instance of the specified class
"""


def is_same_class(obj, a_class):
    """ Function that returns True/False if obj is a type of a_class

    Args:
        obj: object
        a_class: class type

    Returns:
        True if type of obj is a_class
        False, otherwise
    """
    if type(obj) is a_class:
        return True
    else:
        return False
