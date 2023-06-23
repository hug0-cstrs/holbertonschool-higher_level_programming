#!/usr/bin/python3
"""A module with a simple function"""
import json


def load_from_json_file(filename):
    """A function that creates an object from a JSON file.

    Args:
        filename (str): The name of the file to parse

    Returns:
        The Python object read from the JSON file
    """
    with open(filename, encoding="utf-8") as f:
        return json.load(f)
