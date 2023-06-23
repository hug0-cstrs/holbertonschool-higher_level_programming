#!/usr/bin/python3
"""A module with a function that reads a file"""


def read_file(filename=""):
    """A function that reads a text file (UTF8) and prints it to stdout.

    Args:
        filename (str): The name of the file to open. Optional. Defaults to
        an empty string.

    Returns: nothing
    """
    with open(filename, 'r', encoding="utf-8") as f:
        for line in f:
            print(line, end='')
