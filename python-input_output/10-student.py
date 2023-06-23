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

    def to_json(self, attrs=None):
        """ Method that returns directory description """
        my_dict = {}
        if attrs is not None:
            for key in range(0, len(attrs)):
                if attrs[key] in self.__dict__:
                    my_dict[attrs[key]] = self.__dict__[attrs[key]]
                    key += 1
        else:
            for i in self.__dict__:
                my_dict[i] = self.__dict__[i]
        return my_dict
