#!/usr/bin/python3
"""A module with a function that appends a string at the end of a text file"""


def append_write(filename="", text=""):
    """A function that appends a string at the end of a text file

    Args:
        filename (str): The name of the file to open. Optional. Defaults to
        an empty string.
        text (str): the text to write. Optional. Defaults to an empty string.

    Returns: the number of characters added
    """
    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
