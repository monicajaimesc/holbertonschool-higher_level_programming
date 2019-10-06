#!/usr/bin/python3
""" Here is a short script to 
test max_integer([..])"""

import unittest
max_integer = __import__('6-max_integer').max_integer

# A testcase is created by subclassing unittest.TestCase
class TestMaxInteger(unittest.TestCase):

    # All tests you make must be passable by the function below
    # The unittest module provides tools for constructing and running tests
    # test_ means it's a method
    def test_upper(self):
        self.assertEqual(max_integer([6, 7, 8, 9]), 9)

    def test_none(self):
        self.assertEqual(max_integer([]), None)

    def test_one(self):
        self.assertEqual(max_integer([2]), 2)

    def test_one_neg(self):
        self.assertEqual(max_integer([-10]), -10)

    def test_neg(self):
        self.assertEqual(max_integer([1, -2, -3, -4]), 1)

    def test_middle(self):
        self.assertEqual(max_integer([1, 3, 8, 2, 6]), 8)

if __name__ == '__main__':
    unittest.main()

# The crux of each test is a call to assertEqual() to check 
# for an expected result; assertTrue() or assertFalse() to verify a condition; 
# or assertRaises() to verify that a specific exception gets raised. 
# These methods are used instead of the assert statement so 
# the test runner can accumulate all test results and produce a report.
