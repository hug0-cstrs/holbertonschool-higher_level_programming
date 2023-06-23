#!/usr/bin/python3
"""A module with a function that reads a file"""


def write_file(filename="", text=""):
    """A function that reads a text file (UTF8) and prints it to stdout.

    Args:
        filename (str): The name of the file to open. Optional. Defaults to
        an empty string.
        text (str): the text to write. Optional. Defaults to an empty string.

    Returns: the number of characters written to the file
    """
    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
