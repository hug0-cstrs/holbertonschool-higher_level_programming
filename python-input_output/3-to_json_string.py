#!/usr/bin/python3
"""A module with a simple function"""
import json


def to_json_string(my_obj):
    """A function that returns the JSON representation of an object (string).

    Args:
        my_obj (any Python object): the object to turn into JSON

    Returns:
        The JSON representation of an object
    """
    return json.dumps(my_obj)
