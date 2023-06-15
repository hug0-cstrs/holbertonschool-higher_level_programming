#!/usr/bin/python3
"""
This is the "Say My Name" module.

The Say My Name module takes one required parameter and one optional.
It prints "My name is (first) (last)" where (first) and (last) are the args.
"""


def say_my_name(first_name, last_name=""):
    """Print My name is (first) (last) if given, else print error
    """
    if type(first_name) is not str or first_name is None:
        raise TypeError("first_name must be a string")
    elif type(last_name) is not str or last_name is None:
        raise TypeError("last_name must be a string")
    else:
        print("My name is {} {}".format(first_name, last_name))
