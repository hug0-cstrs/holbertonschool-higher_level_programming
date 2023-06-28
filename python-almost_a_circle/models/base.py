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
        if list_objs is None:
            list_objs = []

        my_dict = []
        for obj in list_objs:
            my_dict.append(obj.to_dictionary())
        obj = cls.to_json_string(my_dict)
        filename = cls.__name__ + ".json"
        with open(filename, "w") as jsonfile:
            jsonfile.write(obj)

    @staticmethod
    def from_json_string(json_string):
        """Static method that returns the list of the JSON string
        representation json_string
        """
        if json_string is None:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Class method that returns an instance
        with all attributes already set
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(2, 2)
        if cls.__name__ == "Square":
            dummy = cls(7)

        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Return a list of classes instantiated from a file of JSON strings.

        Reads from `<cls.__name__>.json`.

        Returns:
            If the file does not exist - an empty list.
            Otherwise - a list of instantiated classes.
        """
        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, "r") as jsonfile:
                list_dicts = Base.from_json_string(jsonfile.read())
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []
