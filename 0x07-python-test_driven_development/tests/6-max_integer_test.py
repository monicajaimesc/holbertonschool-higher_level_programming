#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    def test_max_int(self):
        self.assertAlmostEqual(max_integer([1, 2, 3]), 3)

    def test_list_str(self):
        self.asserRaises(TypeError, max_integer([1, "unicorn", 58]))

#In this task, you will write unittests for the function def max_integer(list=[]):.

#Your test file should be inside a folder tests
#You have to use the unittest module
#Your test file should be python files (extension: .py)
#Your test file should be executed by using this command: python3 -m unittest tests.6-max_integer_test
#All tests you make must be passable by the function below
#We strongly encourage you to work together on test cases, so that you don’t miss any edge case
