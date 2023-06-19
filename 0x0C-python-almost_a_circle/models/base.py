#!/usr/bin/python3
"""This module defines the Base class. This project superclass
    will manage the unique id variable accross the project
"""
import json
import csv


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
        if cls.__name__ == 'Square':
            obj = cls(1)
        if cls.__name__ == 'Rectangle':
            obj = cls(1, 1)
        obj.update(**dictionary)
        return obj

    @classmethod
    def load_from_file(cls):
        """Creates a Square or Rectangle instance
            from a string (json) representation
        """
        filename = cls.__name__ + '.json'
        try:
            with open(filename, 'r', encoding='utf-8') as stream:
                my_str = stream.read()
        except FileNotFoundError:
            my_list = []
            return my_list

        my_list = cls.from_json_string(my_str)
        objs_list = [cls.create(**dic) for dic in my_list]
        return objs_list

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Get dictionary representation of an object,
            serialize the dict to CSV, and write
            serialized data to CSV file
        """
        filename = cls.__name__ + '.csv'
        if list_objs is None:
            my_data = []
        else:
            my_data = [obj.to_dictionary() for obj in list_objs]
            if cls.__name__ == 'Rectangle':
                fields = ['id', 'width', 'height', 'x', 'y']
            if cls.__name__ == 'Square':
                fields = ['id', 'size', 'x', 'y']
        with open(filename, 'w', encoding='utf-8') as stream:
            csv_stream = csv.DictWriter(stream, fieldnames = fields)
            csv_stream.writeheader()
            csv_stream.writerows(my_data)

    @classmethod
    def load_from_file_csv(cls):
        """Create an instance or list of instances
            from a csv file
        """
        filename = cls.__name__ + '.csv'
        try:
            with open(filename, 'r') as stream:
                csv_stream = csv.DictReader(stream)
                my_dicts = [dic for dic in csv_stream]
                true_dict = []
                for dic in my_dicts:
                    for key in dic:
                        dic[key] = int(dic[key])
                    true_dict.append(dic)
                my_objs = [cls.create(**dic) for dic in true_dict]
        except FileNotFoundError:
            my_objs = []
        return my_objs
