#!/usr/bin/python3
"""A module with a function that check if the object is an instance of,
or if the object is an instance of a class that inherited from
"""


def is_kind_of_class(obj, a_class):
    """ Function that returns True/False if obj is a type of a_class

    Args:
        obj: object
        a_class: class type

    Returns:
        True if the object is an instance of,
        or if the object is an instance of a class that inherited from
        False, otherwise
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
