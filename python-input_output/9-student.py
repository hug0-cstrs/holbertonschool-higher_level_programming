#!/usr/bin/python3
"""A module with a simple function"""


class Student:
    def __init__(self, first_name, last_name, age):
        """A Student initialisation contructor method.

        Args:
            first_name (str): Student first name
            last_name (str): Student last name
            age (int): Student age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ Method that returns directory description """
        return self.__dict__.copy()
