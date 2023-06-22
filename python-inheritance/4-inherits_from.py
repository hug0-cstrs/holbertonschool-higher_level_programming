#!/usr/bin/python3
"""A module with a function that check if the object is an instance of a class
that inherited (directly or indirectly) from the specified class
"""


def inherits_from(obj, a_class):
    """ Function that returns True/False if obj is a type of a_class

    Args:
        obj: object
        a_class: class type

    Returns:
        True, if the object is an instance of a class that inherited
        (directly or indirectly) from the specified class
        False, otherwise
    """
    if type(obj) is not a_class:
        return issubclass(type(obj), a_class)
    else:
        return False
