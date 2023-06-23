#!/usr/bin/python3
"""A module with a simple function"""
import json


def from_json_string(my_str):
    """A function that returns the JSON representation of an object (string).

    Args:
        my_obj (any Python object): the object to turn into JSON

    Returns:
        The JSON representation of an object
    """
    return json.loads(my_str)
