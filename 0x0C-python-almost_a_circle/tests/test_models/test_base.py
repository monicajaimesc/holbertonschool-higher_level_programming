#!/usr/bin/python3
"""Moudel for base to test with unittest"""

import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import json



class Test_base(unittest.TestCase):
    """test for base clase"""
    def test_is_subclass(self):
        """ test instance """
        r = Base(1)
        # assertIsintance () Test that obj is
        # (or is not) an instance of cls
        self.assertIsInstance(r, Base)
        # Test that expresion is (or is not) None.
        self.assertIsNot(r, Base)

    def test_id(self):
        """ test base ID """
        # id 1
        b1 = Base()
        # Test that first and second are equal
        # a == b
        self.assertEqual(b1.id, 1)
        self.assertEqual(b1.id, Base._Base__nb_objects)
        # id 2
        b2 = Base()
        self.assertEqual(b2.id, 2)
        self.assertEqual(b2.id, Base._Base__nb_objects)
        b3 = Base(12)
        self.assertEqual(b3.id, 12)
        # we didn't tested for integers
        b4 = Base("string")
        self.assertEqual(b4.id, "string")
        b5 = Base({id: 1})
        self.assertEqual(b5.id, {id: 1})
        # not a number
        # interpreted as a value
        # that is undefined or unrepresentable
        b6 = Base(float('NaN'))
        # a != b
        self.assertNotEqual(b6.id, b6.id)
        b7 = Base([2])
        self.assertEqual(b7.id, [2])
        b8 = Base(3.4)
        self.assertEqual(b8.id, 3.4)
        b9 = Base((3, 4))
        self.assertEqual(b9.id, (3, 4))
        b10 = Base({3, 4})
        self.assertEqual(b10.id, {3, 4})
        # id 3
        b11 = Base(None)
        self.assertEqual(b11.id, 3)
        self.assertEqual(b11.id, Base._Base__nb_objects)

    def test_to_json_string(self):
        """test to_json_string method"""
        # If list_dictionaries is None or empty, return the string: "[]"
        Base._Base__nb_objects = 0
        r1 = Rectangle(10, 7, 2, 8)
        # You can try to do json.loads(), which will throw a ValueError 
        # if the string you pass can't be decoded as JSON.
        json_dict = Base.to_json_string([r1.to_dictionary()])
        self.assertEqual(type(json_dict), str)
        list_dict = json.loads(json_dict)
        list = [{"x": 2, "width": 10, "id": 1, "height": 7, "y": 8}]
        # to check for an expected result;
        self.assertEqual(list_dict, list)

    def test_save_to_file_rectangle(self):
        """test save to file method"""
        Base._Base__nb_objects = 0
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as file:
            data = file.read()
        expectData = [{"y": 8, "x": 2, "id": 1, "width": 10, "height": 7},
                      {"y": 0, "x": 0, "id": 2, "width": 2, "height": 4}]
        list_dict = json.loads(data)
        self.assertDictEqual(list_dict[0], expectData[0])
        self.assertDictEqual(list_dict[1], expectData[1])

        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as file:
            data = file.read()
        expectData = "[]"
        self.assertEqual(data, expectData)

    def test_save_to_file_square(self):
        """test save to file method"""
        Base._Base__nb_objects = 0
        r1 = Square(10, 2, 8)
        r2 = Square(2, 4)
        Square.save_to_file([r1, r2])
        with open("Square.json", "r") as file:
            data = file.read()
        expectData = [{"y": 8, "x": 2, "id": 1, "size": 10},
                      {"y": 0, "x": 4, "id": 2, "size": 2}]
        list_dict = json.loads(data)
        self.assertDictEqual(list_dict[0], expectData[0])
        self.assertDictEqual(list_dict[1], expectData[1])

        Square.save_to_file(None)
        with open("Square.json", "r") as file:
            data = file.read()
        expectData = "[]"
        self.assertEqual(data, expectData)

        Square.save_to_file([Square(1)])
        with open("Square.json", "r") as file:
            data = file.read()
        list_dict = json.loads(data)
        expectData = [{'y': 0, 'x': 0, 'id': 3, 'size': 1}]
        self.assertDictEqual(list_dict[0], expectData[0])

        Square.save_to_file([])
        with open("Square.json", "r") as file:
            data = file.read()
        list_dict = json.loads(data)
        expectData = []
        self.assertEqual(list_dict, expectData)

    def test_save_to_file_diff_dataType_Rectangle(self):
        """test save_to_file method with different datatype"""
        with self.assertRaises(TypeError):
            Rectangle.save_to_file(2)
        with self.assertRaises(Exception):
            Rectangle.save_to_file("23")
        with self.assertRaises(Exception):
            Rectangle.save_to_file({1})
        with self.assertRaises(Exception):
            Rectangle.save_to_file({'key': 1})
        with self.assertRaises(TypeError):
            Rectangle.save_to_file(True)
        with self.assertRaises(TypeError):
            Rectangle.save_to_file(False)
        with self.assertRaises(TypeError):
            Rectangle.save_to_file(2.3)
        with self.assertRaises(TypeError):
            Rectangle.save_to_file(float('nan'))
        with self.assertRaises(TypeError):
            Rectangle.save_to_file(float('inf'))

    def test_save_to_file_diff_dataType_square(self):
        """test save_to_file method with different datatype"""
        with self.assertRaises(TypeError):
            Square.save_to_file(2)
        with self.assertRaises(Exception):
            Square.save_to_file("23")
        with self.assertRaises(Exception):
            Square.save_to_file({1})
        with self.assertRaises(Exception):
            Square.save_to_file({'key': 1})
        with self.assertRaises(TypeError):
            Square.save_to_file(True)
        with self.assertRaises(TypeError):
            Square.save_to_file(False)
        with self.assertRaises(TypeError):
            Square.save_to_file(2.3)
        with self.assertRaises(TypeError):
            Square.save_to_file(float('nan'))
        with self.assertRaises(TypeError):
            Square.save_to_file(float('inf'))

    def test_from_json_string_success(self):
        """test from_json_string method"""
        Base._Base__nb_objects = 0
        list_input = [{'id': 89, 'width': 10, 'height': 4},
                      {'id': 7, 'width': 1, 'height': 7}]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(type(list_output), list)
        self.assertDictEqual(list_output[0], list_input[0])
        self.assertDictEqual(list_output[1], list_input[1])

        list_output = Rectangle.from_json_string(None)
        self.assertEqual(type(list_output), list)
        self.assertEqual(list_output, [])

    def test_from_json_string_diff_dataType(self):
        """test test_from_json_string method with different datatype"""
        with self.assertRaises(ValueError):
            Rectangle.from_json_string("a")
        with self.assertRaises(TypeError):
            Rectangle.from_json_string(True)
        with self.assertRaises(TypeError):
            Rectangle.from_json_string(False)
        with self.assertRaises(TypeError):
            Rectangle.from_json_string({1})
        with self.assertRaises(TypeError):
            Rectangle.from_json_string(2.3)
        with self.assertRaises(TypeError):
            Rectangle.from_json_string(2)
        with self.assertRaises(TypeError):
            Rectangle.from_json_string({'key': 1})
        with self.assertRaises(TypeError):
            Rectangle.from_json_string(float('nan'))
        with self.assertRaises(TypeError):
            Rectangle.from_json_string(float('inf'))

    def test_from_json_string_diff_key(self):
        """test from_json_string with different key"""
        list_input = [{'i': 89, 'w': 10, 'h': 4},
                      {'i': 7, 'w': 1, 'h': 7}]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(type(list_output), list)
        self.assertDictEqual(list_output[0], list_input[0])
        self.assertDictEqual(list_output[1], list_input[1])

    def test_create(self):
        """test create method"""
        Base._Base__nb_objects = 0
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertNotEqual(r1, r2)
        self.assertEqual(r1.__str__(), "[Rectangle] (1) 1/0 - 3/5")
        self.assertEqual(r2.__str__(), "[Rectangle] (1) 1/0 - 3/5")

    def test_create_diff_dataType(self):
        """test create with different datatype"""
        with self.assertRaises(TypeError):
            r2 = Rectangle.create({2})
        with self.assertRaises(TypeError):
            r2 = Rectangle.create("2")
        with self.assertRaises(TypeError):
            r2 = Rectangle.create([2])
        with self.assertRaises(TypeError):
            r2 = Rectangle.create(2)
        with self.assertRaises(TypeError):
            r2 = Rectangle.create(2.3)
        with self.assertRaises(TypeError):
            r2 = Rectangle.create(True)
        with self.assertRaises(TypeError):
            r2 = Rectangle.create(False)
        with self.assertRaises(TypeError):
            r2 = Rectangle.create(None)
        with self.assertRaises(TypeError):
            r2 = Rectangle.create(float('nan'))
        with self.assertRaises(TypeError):
            r2 = Rectangle.create(float('inf'))

    def test_load_from_file(self):
        """test load_from_file method"""

        """Rectangle"""
        Base._Base__nb_objects = 0
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_rect_input = [r1, r2]
        Rectangle.save_to_file(list_rect_input)
        list_rect_output = Rectangle.load_from_file()
        self.assertNotEqual(id(list_rect_input[0]), id(list_rect_output[0]))
        self.assertNotEqual(id(list_rect_input[1]), id(list_rect_output[1]))
        self.assertNotEqual(id(list_rect_output[0]), id(list_rect_output[1]))
        self.assertEqual(list_rect_output[0].__str__(),
                         "[Rectangle] (1) 2/8 - 10/7")
        self.assertEqual(list_rect_output[1].__str__(),
                         "[Rectangle] (2) 0/0 - 2/4")
        """square"""
        s1 = Square(5)
        s2 = Square(7, 9, 1)
        list_sq_input = [s1, s2]
        Square.save_to_file(list_sq_input)
        list_sq_output = Square.load_from_file()
        self.assertNotEqual(id(list_sq_input[0]), id(list_sq_output[0]))
        self.assertNotEqual(id(list_sq_input[1]), id(list_sq_output[1]))
        self.assertNotEqual(id(list_sq_output[0]), id(list_sq_output[1]))
        self.assertEqual(list_sq_output[0].__str__(),
                         "[Square] (5) 0/0 - 5")
        self.assertEqual(list_sq_output[1].__str__(),
                         "[Square] (6) 9/1 - 7")


if __name__ == '__main__':
    unittest.main()
