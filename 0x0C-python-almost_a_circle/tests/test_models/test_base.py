#!/usr/bin/python3
"""Moudel for base to test with unittest"""

import unittest
from models.base import Base


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
