#!/usr/bin/python3
"""
This module contains the Base class.

It contains a private class attribute __nb_objects and a class constructor __init__.
It provides methods for JSON string representation of list dictionaries, saving JSON strings of instance dictionaries into files,
returning Python objects from JSON string representations, creating instances with attributes already set,
returning lists of instances, and saving to and loading from CSV files.
"""

import json
import csv


class Base:
    """
    Defines the Base class.

    Class Attributes:
        __nb_objects

    Methods:
        __init__(self, id=None)

    Static Methods:
        to_json_string(list_dictionaries)
        from_json_string(json_string)

    Class Methods:
        save_to_file(cls, list_objs)
        save_to_file_csv(cls, list_objs)
        load_from_file(cls)
        load_from_file_csv(cls)
        create(cls, **dictionary)
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes id, increments the class attribute if no id is provided, and sets it as id.
        """
        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns a JSON string representation of a list of dictionaries.
        """
        if list_dictionaries is None:
            list_dictionaries = []
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """
        Returns a Python object from a JSON string representation.
        """
        if json_string is None or len(json_string) == 0:
            json_string = "[]"
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Saves JSON strings of all instances into a file.
        """
        objs = []
        if list_objs is not None:
            for o in list_objs:
                objs.append(cls.to_dictionary(o))
        filename = cls.__name__ + ".json"
        with open(filename, "w") as f:
            f.write(cls.to_json_string(objs))

    @classmethod
    def create(cls, **dictionary):
        """
        Returns an instance with attributes already set.
        """
        if cls.__name__ == "Square":
            dummy = cls(1)
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """
        Returns a list of instances.
        """
        filename = cls.__name__ + ".json"
        instances_list = []
        try:
            with open(filename, "r") as f:
                instances = cls.from_json_string(f.read())
            for instance_dict in instances:
                instances_list.append(cls.create(**instance_dict))
        except:
            pass
        return instances_list

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        Saves instances to a CSV file.
        """
        filename = cls.__name__ + ".csv"
        with open(filename, 'w', newline='') as f:
            writer = csv.writer(f)
            for o in list_objs:
                if cls.__name__ == "Rectangle":
                    writer.writerow([o.id, o.width, o.height, o.x, o.y])
                if cls.__name__ == "Square":
                    writer.writerow([o.id, o.size, o.x, o.y])

    @classmethod
    def load_from_file_csv(cls):
        """
        Loads instances from a CSV file.
        """
        objs = []
        filename = cls.__name__ + ".csv"
        with open(filename, 'r', newline='') as f:
            reader = csv.reader(f)
            for row in reader:
                if cls.__name__ == "Rectangle":
                    dic = {"id": int(row[0]),
                           "width": int(row[1]),
                           "height": int(row[2]),
                           "x": int(row[3]),
                           "y": int(row[4])}
                if cls.__name__ == "Square":
                    dic = {"id": int(row[0]),
                           "size": int(row[1]),
                           "x": int(row[2]),
                           "y": int(row[3])}
                o = cls.create(**dic)
                objs.append(o)
        return objs
