#!/usr/bin/python3
"""
Class model - Base
"""
import json


class Base:
    """Define Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize class constructor"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return JSON string representation"""
        if list_dictionaries is None or list_dictionaries == []:
            return json.dumps([])
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs=None):
        """Save JSON string to file"""
        with open(cls.__name__+".json", 'w') as f:
            if list_objs == None or list_objs == []:
                json.dump([], f)
            else:
                jstr = cls.to_json_string(
                    [l.to_dictionary() for l in list_objs])
                json.dump(json.loads(jstr), f)

    @staticmethod
    def from_json_string(json_string):
        """Transform JSON to String"""
        if json_string == None or json_string == []:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Return an instance with all attributes already set"""
        if cls.__name__ == "Square":
            dummy_instance = (1)
        if cls.__name__ == "Rectangle":
            dummy_instance = cls(1, 1)
        dummy_instance.update(**dictionary)
        return dummy_instance

    @classmethod
    def load_from_file(cls):
        """Load JSON string from file"""
        try:
            with open(cls.__name__+".json", "r") as f:
                d = cls.from_json_string(f.read())
                return [cls.create(**x) for x in d]
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        with open(cls.__name__+".csv", 'w') as f:
            if list_objs == None or list_objs == []:
                json.dump([], f)
            else:

                jstr = cls.to_json_string(
                    [l.to_dictionary_csv() for l in list_objs])
                json.dump(json.loads(jstr), f)

    @classmethod
    def load_from_file_csv(cls):
        try:
            with open(cls.__name__+".csv", "r") as f:
                d = cls.from_json_string(f.read())
                if cls.__name__ == "Square":
                    return [cls(**dt) for dt in d]
                if cls.__name__ == "Rectangle":
                    return [cls(**dt) for dt in d]
        except FileNotFoundError:
            return []
