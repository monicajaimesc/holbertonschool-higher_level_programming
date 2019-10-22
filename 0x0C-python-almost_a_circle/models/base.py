#!/usr/bin/python3
"""
Base module that contain the first class Base
"""
import json
"""import Json"""


class Base:
    """
    This class will be the “base” of all other
    classes in this project.
    """
    # private class attribute
    __nb_objects = 0

    def __init__(self, id=None):
        """__init__ method:
        class constructor with its
        assign the public instance attribute id
        Args:
            id - value greater than 0
        """
        if id is not None:
            # b = base (12)
            # public instance attribute
            self.id = id
        else:
            Base.__nb_objects += 1
            # assign the new value to the public instance attribute id
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """"to_json_string: Serialize obj to a JSON
        formatted str.
        Args:
            list_dictionaries: a list of dictionaries
        Return:
            returns the JSON string representation[] of a list_dictionarires
        """
        # If list_dictionaries is None or empty, return the string: "[]"
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return '[]'
        # Serialize obj to a JSON formatted str.
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        save_to_file classmethod: writes the Kson string
        representation of list_objs to a file
        Args:
            cls: the class itself
            list_objs: a list of instances who inherits of Base
        """
        # <Class name>.json - example: Rectangle.json
        filename = "{}.json".format(cls.__name__)
        with open(filename, mode='w', encoding='utf-8') as f:
            # If list_objs is None, save an empty list
            if list_objs is None:
                f.write('[]')
            else:
                # You must overwrite the file if it already exists
                # to_dictionary(self) that returns the dictionary
                # representation of a Square:
                list_dict = [obj.to_dictionary()for obj in list_objs]
                # json_string returns the JSON string representation
                # of list_dictionaries:
                f.write(cls.to_json_string(list_dict))

    @staticmethod
    def from_json_string(json_string):
        """ from_json_string static method: Desearialize
        JSON string to object
        Args:
            json_string: a string representing a list of
            dictionaries
        Return:
        returns the list of the JSON string representation
        json_string
        """
        # If json_string is None or empty, return an empty list
        if json_string is None or len(json_string) == 0:
            return []
        # Decoding JSON:
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """create classmethod: Dictionary to Instance
        Args:
            cls: the class itself
            dictionary: LIKE A double pointer to a dictionary
        Return:
            returns an instance with all atributes
            already set
        """
        # create a Rectangle instance with dummy attrubutes
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1, 1, 1)
        if cls.__name__ == "Square":
            dummy = cls(1, 1, 1)
        # Call update instance method to this “dummy” instance
        # to apply your real values
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """
        load_from_file - load the file and return a new list to exec
        """
        # Create the namefile
        file_name = str(cls.__name__) + ".json"
        # Try to open the file
        try:
            # Read the file
            with open(file_name, mode="r", encoding="utf-8") as f:
                # Create empty file
                new_list = []
                # Read the file
                read_file = f.read()
                new_file = cls.from_json_string(read_file)
                for dic in new_file:
                    new_inst = cls.create(**dic)
                    new_list.append(new_inst)
                return new_list
        except Exception:
            return []
