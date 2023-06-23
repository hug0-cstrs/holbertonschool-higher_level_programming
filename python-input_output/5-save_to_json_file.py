#!/usr/bin/python3
"""A module with a simple function"""
import json


def save_to_json_file(my_obj, filename):
    """A function that writes an Object to a text file,
    using a JSON representation.

    Args:
        my_obj (obj): The object to write to the file
        filename (file): the file where we need to write the object to

    Return: nothing
    """
    with open(filename, encoding="utf-8") as f:
        return f.write(json.dumps(my_obj))
