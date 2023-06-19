#!/usr/bin/python3
"""This module defines the Base class. This project superclass
    will manage the unique id variable accross the project
"""
import json


class Base:
    """This Base class is the main superclass
        and will manage id for all objects
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """This special method will initialize
            the id variable
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Serialize a list object
            to a json string
        """
        if list_dictionaries is None:
            list_dictionaries = []
        my_obj = json.dumps(list_dictionaries)
        return my_obj

    @classmethod
    def save_to_file(cls, list_objs):
        """Serialize a list object and write
            the result to a file
        """
        filename = cls.__name__ + '.json'
        if list_objs is None:
            list_objs = []
        list_dictionaries = [obj.to_dictionary() for obj in list_objs]
        serial = cls.to_json_string(list_dictionaries)
        with open(filename, 'w', encoding='utf-8') as stream:
            stream.write(serial)

    @staticmethod
    def from_json_string(json_string):
        """Deserialize a json (string) object
            and return it
        """
        if json_string is None or len(json_string) < 1:
            my_obj = []
        else:
            my_obj = json.loads(json_string)
        return my_obj

    @classmethod
    def create(cls, **dictionary):
        """Create a Rectangle or Square object
            from a dictionary representation
        """
        obj = cls(1, 1)
        obj.update(**dictionary)
        return obj

    @classmethod
    def load_from_file(cls):
        """Creates a Square or Rectangle instance
            from a string (json) representation
        """
        filename = cls.__name__ + '.json'
        with open(filename, 'r+', encoding='utf-8') as stream:
            my_str = stream.read()
        my_list = cls.from_json_string(my_str)
        objs_list = [cls.create(**dic) for dic in my_list]
        return objs_list
