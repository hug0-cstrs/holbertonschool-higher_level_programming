#!/usr/bin/python3
"""""A module with a simple class"""""
import json


class Base:
    """This class will be the “base” of all other classes in this project.
    The goal of it is to manage id attribute in all your future classes and
    to avoid duplicating the same code (by extension, same bugs)
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        This is a constructor function that assigns an ID to an object either
        based on a given ID or by incrementing a counter.

        Args:
            id (int): The "id" parameter is an optional argument that can
            be passed to the constructor of an object. If a value is provided
            for "id", it will be assigned to the object's "id" attribute.
            If no value is provided for "id", a new value will be generated
            and assigned to.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Static method that returns the JSON string representation of
        list_dictionaries
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Class method that writes the JSON string representation of
        list_objs to a file
        """
        if list_objs is not None and len(list_objs) > 0:
            empty_list = []
            filename = "{}.json".format(cls.__name__)
            for i in list_objs:
                my_dict = i.to_dictionary()
                empty_list.append(my_dict)
            with open(filename, 'w') as jsonfile:
                jsonfile.write(cls.to_json_string(empty_list))
        else:
            with open(filename, 'w') as jsonfile:
                jsonfile.write(cls.to_json_string(list_objs))
