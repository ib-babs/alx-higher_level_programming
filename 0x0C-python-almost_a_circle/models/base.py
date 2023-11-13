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
            return "[]"
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
        dummy_instance = cls(1, 9, 3)
        if cls.__name__ == "Square":
            size = dictionary["size"]
            x = dictionary["x"]
            y = dictionary["y"]
            id = dictionary["id"]
            dummy_instance.update(size=size, x=x, y=y, id=id)
            return dummy_instance

        if cls.__name__ == "Rectangle":
            width = dictionary["width"]
            height = dictionary["height"]
            x = dictionary["x"]
            y = dictionary["y"]
            id = dictionary["id"]
            dummy_instance.update(width=width, height=height,
                                  x=x, y=y, id=id)
            return dummy_instance

    # @classmethod
    # def load_from_file(cls):
    #     """Load JSON string from file"""
    #     with open(cls.__name__+".json") as f:
    #         if not f:
    #             return []
    #         else:
    #             #print(cls.from_json_string([j for j in json.load(f)]))
    #             for j in json.load(f):
    #                 print(cls.from_json_string(j))
