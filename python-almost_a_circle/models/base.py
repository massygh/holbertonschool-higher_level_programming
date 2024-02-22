#!/usr/bin/python3
""" Module that contains class Base """
import json


class Base:
    """ Base class """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Convert a list"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ Save a list of objects to a file in JSON format """
        filename = cls.__name__ + ".json"
        list_of_dict = []
        if list_objs is not None:
            for obj in list_objs:
                list_of_dict.append(obj.to_dictionary())
        with open(filename, "w", encoding="UTF-8") as file:
            file.write(cls.to_json_string(list_of_dict))

    @staticmethod
    def from_json_string(json_string):
        """ Convert a JSON """
        if json_string is None or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ Create a new instance of the class from a dictionary """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        else:
            dummy = cls()

        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances"""
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r") as file:
                json_string = file.read()
                dictionaries = cls.from_json_string(json_string)
                instances = [cls.create(**dictionary)
                             for dictionary in dictionaries]
            return instances
        except FileNotFoundError:
            return []
