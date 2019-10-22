"""Unittest for class Square
"""

import unittest
import sys
import io
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestSquareClass(unittest.TestCase):
    def test_is_subclass(self):
        """test Square is subclass of Base or not"""
        r = Square(1, 1)
        self.assertIsInstance(r, Base)
        self.assertIsNot(r, Base)

    def test_id_no_input(self):
        """test id with no input"""
        Base._Base__nb_objects = 0
        b1 = Square(1, 1, 1)
        self.assertEqual(b1.id, 1)
        self.assertEqual(b1.id, Square._Base__nb_objects)
        b2 = Square(1, 1, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b2.id, Square._Base__nb_objects)

    def test_id_datatype(self):
        """test id with different data type"""
        Base._Base__nb_objects = 0
        b3 = Square(1, 1, 1, 12)
        self.assertEqual(b3.id, 12)
        b4 = Square(1, 1, 1, "string")
        self.assertEqual(b4.id, "string")
        b5 = Square(1, 1, 1, {id: 1})
        self.assertEqual(b5.id, {id: 1})
        b7 = Square(1, 1, 1, [1])
        self.assertEqual(b7.id, [1])
        b8 = Square(1, 1, 1, 2.4)
        self.assertEqual(b8.id, 2.4)
        b9 = Square(1, 1, 1, (1, 2))
        self.assertEqual(b9.id, (1, 2))
        b10 = Square(1, 1, 1, {1, 2})
        self.assertEqual(b10.id, {1, 2})
        b11 = Square(1, 1, 1, True)
        self.assertEqual(b11.id, True)
        b12 = Square(1, 1, 1, False)
        self.assertEqual(b12.id, False)
        bN = Square(1, 1, 1, None)
        self.assertEqual(bN.id, 1)
        self.assertEqual(bN.id, Square._Base__nb_objects)

    def test_id_special_case(self):
        """test id with special cases"""
        b6 = Square(1, 1, 1, float('nan'))
        self.assertNotEqual(b6.id, b6.id)
        b6 = Square(1, 1, 1, float('inf'))
        self.assertEqual(b6.id, float('inf'))

    def test_size_int_success(self):
        """test size with integer that is greater than 0"""
        b1 = Square(2)
        self.assertEqual(b1.size, 2)
        self.assertEqual(b1.width, 2)
        self.assertEqual(b1.height, 2)
        b2 = Square(4, 1, 1)
        self.assertEqual(b2.size, 4)
        self.assertEqual(b2.width, 4)
        self.assertEqual(b2.height, 4)
        b3 = Square(23, 1, 12)
        self.assertEqual(b3.size, 23)
        self.assertEqual(b3.width, 23)
        self.assertEqual(b3.height, 23)

    def test_size_int_fail(self):
        """test width and height with integer that is equal or less
        than 0
        """
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(-1, 1)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(0, -1)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(size=-1)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(size=0)

    def test_size_special_case(self):
        """test width and height with special cases"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(float('nan'), 1)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(float('inf'), 1)

    def test_size_isInt(self):
        """test size with non int data type"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("a", 1)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square({1}, 1)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square([1], 1)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square({1: 2}, 1)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square((1, 2), 1)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(True, 1)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(False, 1)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(None, 1)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("a", "b")
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(1.5, 2)

    def test_x_y_int_success(self):
        """test x and y with integer that is greater or equal 0"""
        b1 = Square(2, 2, 2)
        self.assertEqual(b1.x, 2)
        self.assertEqual(b1.y, 2)
        b2 = Square(4, 3, 4)
        self.assertEqual(b2.x, 3)
        self.assertEqual(b2.y, 4)
        b3 = Square(40, 23, 40, 12)
        self.assertEqual(b3.x, 23)
        self.assertEqual(b3.y, 40)
        b4 = Square(40, 0, 0, 0)
        self.assertEqual(b4.x, 0)
        self.assertEqual(b4.y, 0)

    def test_x_y_int_fail(self):
        """test x and y with integer that is less
        than 0
        """
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Square(1, -2)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Square(1, 1, -2)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Square(1, -1, -1)

    def test_x_y_special_case(self):
        """test x and y with special cases"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, float('nan'), 1)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, float('inf'), 1)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 1, float('nan'), 1)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 1, float('inf'), 1)

    def test_x_isInt(self):
        """test x with non int data type"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, "a", 1)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, {1}, 1)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, [1], 1)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, {1: 2}, 1)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, (1, 2), 1)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, True, 1)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, False, 1)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, None, 1)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, "a", "b")
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, 1.5, 2)

    def test_y_isInt(self):
        """test y with non int data type"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 1, "a")
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 1, {1, 2})
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 1, [1, 2])
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 1, {1: 2})
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 1, (1, 2))
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 1, True)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 1, False)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 1, None)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, "a", "b")
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 1, 2.4)

    def test_area(self):
        """test area of Square"""
        self.assertEqual(Square(3).area(), 9)
        self.assertEqual(Square(2, 0).area(), 4)
        self.assertEqual(Square(2, 2, 0, 0).area(), 4)

    def test_display(self):
        """test display method"""
        out = io.StringIO()
        sys.stdout = out
        Square(2).display()
        output = out.getvalue()
        self.assertEqual(output, "##\n##\n")

        out = io.StringIO()
        sys.stdout = out
        Square(3).display()
        output = out.getvalue()
        self.assertEqual(output, "###\n###\n###\n")

        out = io.StringIO()
        sys.stdout = out
        Square(3, 1, 1).display()
        output = out.getvalue()
        self.assertEqual(output, "\n ###\n ###\n ###\n")

        out = io.StringIO()
        sys.stdout = out
        Square(3, 2, 3).display()
        output = out.getvalue()
        self.assertEqual(output, "\n\n\n  ###\n  ###\n  ###\n")

        out = io.StringIO()
        sys.stdout = out
        Square(3, 0, 0).display()
        output = out.getvalue()
        self.assertEqual(output, "###\n###\n###\n")

    def test_str(self):
        """test str method"""
        Base._Base__nb_objects = 0
        r1 = Square(6, 2, 1, 12)
        self.assertEqual(str(r1), "[Square] (12) 2/1 - 6")
        r2 = Square(5, 1)
        self.assertEqual(str(r2), "[Square] (1) 1/0 - 5")
        r3 = Square(1, 2, 4)
        self.assertEqual(str(r3), "[Square] (2) 2/4 - 1")

    def test_update_int_success(self):
        """test update method"""
        Base._Base__nb_objects = 0
        r1 = Square(10, 10, 10)
        self.assertEqual(str(r1), "[Square] (1) 10/10 - 10")
        r1.update(89)
        self.assertEqual(str(r1), "[Square] (89) 10/10 - 10")
        r1.update(89, 2)
        self.assertEqual(str(r1), "[Square] (89) 10/10 - 2")
        r1.update(89, 2, 3)
        self.assertEqual(str(r1), "[Square] (89) 3/10 - 2")
        r1.update(89, 2, 3, 4)
        self.assertEqual(str(r1), "[Square] (89) 3/4 - 2")

    def test_update_id_noKeyword(self):
        """test update id with no-keyword argument"""
        Base._Base__nb_objects = 0
        r1 = Square(10, 10, 10)
        self.assertEqual(str(r1), "[Square] (1) 10/10 - 10")
        r1.update("string")
        self.assertEqual(str(r1), "[Square] (string) 10/10 - 10")
        r1.update([1])
        self.assertEqual(str(r1), "[Square] ([1]) 10/10 - 10")
        r1.update({1})
        self.assertEqual(str(r1), "[Square] ({1}) 10/10 - 10")
        r1.update((1, 1))
        self.assertEqual(str(r1), "[Square] ((1, 1)) 10/10 - 10")
        r1.update({'key': 2})
        self.assertEqual(str(r1), "[Square] ({'key': 2}) 10/10 - 10")
        r1.update(2.4)
        self.assertEqual(str(r1), "[Square] (2.4) 10/10 - 10")
        r1.update(True)
        self.assertEqual(str(r1), "[Square] (True) 10/10 - 10")
        r1.update(False)
        self.assertEqual(str(r1), "[Square] (False) 10/10 - 10")
        r1.update(None)
        self.assertEqual(str(r1), "[Square] (2) 10/10 - 10")
        r1.update(float('nan'))
        self.assertNotEqual(r1.id, r1.id)
        r1.update(float('inf'))
        self.assertEqual(str(r1), "[Square] (inf) 10/10 - 10")

    def test_update_id_Keyword(self):
        """test update id with keyword argument"""
        Base._Base__nb_objects = 0
        r1 = Square(10, 10, 10)
        self.assertEqual(str(r1), "[Square] (1) 10/10 - 10")
        r1.update(id="string")
        self.assertEqual(str(r1), "[Square] (string) 10/10 - 10")
        r1.update(id=[1])
        self.assertEqual(str(r1), "[Square] ([1]) 10/10 - 10")
        r1.update(id={1})
        self.assertEqual(str(r1), "[Square] ({1}) 10/10 - 10")
        r1.update(id=(1, 1))
        self.assertEqual(str(r1), "[Square] ((1, 1)) 10/10 - 10")
        r1.update(id={'key': 2})
        self.assertEqual(str(r1), "[Square] ({'key': 2}) 10/10 - 10")
        r1.update(id=2.4)
        self.assertEqual(str(r1), "[Square] (2.4) 10/10 - 10")
        r1.update(id=True)
        self.assertEqual(str(r1), "[Square] (True) 10/10 - 10")
        r1.update(id=False)
        self.assertEqual(str(r1), "[Square] (False) 10/10 - 10")
        r1.update(id=None)
        self.assertEqual(str(r1), "[Square] (2) 10/10 - 10")
        r1.update(id=float('nan'))
        self.assertNotEqual(r1.id, r1.id)
        r1.update(id=float('inf'))
        self.assertEqual(str(r1), "[Square] (inf) 10/10 - 10")

    def test_update_size_noKeyword(self):
        """test update size with no-keyword argument"""
        Base._Base__nb_objects = 0
        r1 = Square(10, 10, 10)
        self.assertEqual(str(r1), "[Square] (1) 10/10 - 10")

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r1.update(10, "string")
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r1.update(10, [1])
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r1.update(10, {1})
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r1.update(10, (1, 1))
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r1.update(10, {'key': 2})
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r1.update(10, 2.4)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r1.update(10, True)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r1.update(10, False)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r1.update(10, None)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r1.update(10, float('nan'))
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r1.update(10, float('inf'))

    def test_update_size_Keyword(self):
        """test update size with keyword argument"""
        Base._Base__nb_objects = 0
        r1 = Square(10, 10, 10)
        self.assertEqual(str(r1), "[Square] (1) 10/10 - 10")
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r1.update(size="string")
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r1.update(size=[1])
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r1.update(size={1})
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r1.update(size=(1, 1))
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r1.update(size={'key': 2})
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r1.update(size=2.4)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r1.update(size=True)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r1.update(size=False)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r1.update(size=None)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r1.update(size=float('nan'))
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r1.update(size=float('inf'))

    def test_update_size_int_fail(self):
        """test size with integer that is equal or less
        than 0
        """
        Base._Base__nb_objects = 0
        r1 = Square(10, 10, 10)
        self.assertEqual(str(r1), "[Square] (1) 10/10 - 10")

        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r1.update(0, -1, 1)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r1.update(1, -1, -1)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r1.update(1, 0, 1)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r1.update(size=-1)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r1.update(size=-3)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r1.update(size=0)

    def test_update_x_noKeyword(self):
        """test update x with no-keyword argument"""
        Base._Base__nb_objects = 0
        r1 = Square(10, 10, 10)
        self.assertEqual(str(r1), "[Square] (1) 10/10 - 10")

        r1.update(10, 10, 0)
        self.assertEqual(str(r1), "[Square] (10) 0/10 - 10")

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r1.update(10, 10, "string")
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r1.update(10, 10, [1])
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r1.update(10, 10, {1})
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r1.update(10, 10, (1, 1))
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r1.update(10, 10, {'key': 2})
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r1.update(10, 10, 2.4)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r1.update(10, 10, True)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r1.update(10, 10, False)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r1.update(10, 10, None)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r1.update(10, 10, float('nan'))
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r1.update(10, 10, float('inf'))
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r1.update(20, 10, 2.4, 2.3)

    def test_update_x_Keyword(self):
        """test update x with keyword argument"""
        Base._Base__nb_objects = 0
        r1 = Square(10, 10, 10)
        self.assertEqual(str(r1), "[Square] (1) 10/10 - 10")

        r1.update(x=0)
        self.assertEqual(str(r1), "[Square] (1) 0/10 - 10")

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r1.update(x="string")
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r1.update(x=[1])
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r1.update(x={1})
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r1.update(x=(1, 1))
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r1.update(x={'key': 2})
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r1.update(x=2.4)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r1.update(x=True)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r1.update(x=False)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r1.update(x=None)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r1.update(x=float('nan'))
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r1.update(x=float('inf'))

    def test_update_y_noKeyword(self):
        """test update y with no-keyword argument"""
        Base._Base__nb_objects = 0
        r1 = Square(10, 10, 10)
        self.assertEqual(str(r1), "[Square] (1) 10/10 - 10")

        r1.update(10, 10, 10, 0)
        self.assertEqual(str(r1), "[Square] (10) 10/0 - 10")

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r1.update(10, 10, 10, "string")
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r1.update(10, 10, 10, [1])
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r1.update(10, 10, 10, {1})
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r1.update(10, 10, 10, (1, 1))
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r1.update(10, 10, 10, {'key': 2})
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r1.update(10, 10, 10, 2.4)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r1.update(10, 10, 10, True)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r1.update(10, 10, 10, False)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r1.update(10, 10, 10, None)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r1.update(10, 10, 10, float('nan'))
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r1.update(10, 10, 10, float('inf'))

    def test_update_y_Keyword(self):
        """test update y with keyword argument"""
        Base._Base__nb_objects = 0
        r1 = Square(10, 10, 10)
        self.assertEqual(str(r1), "[Square] (1) 10/10 - 10")

        r1.update(y=0)
        self.assertEqual(str(r1), "[Square] (1) 10/0 - 10")

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r1.update(y="string")
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r1.update(y=[1])
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r1.update(y={1})
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r1.update(y=(1, 1))
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r1.update(y={'key': 2})
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r1.update(y=2.4)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r1.update(y=True)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r1.update(y=False)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r1.update(y=None)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r1.update(y=float('nan'))
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r1.update(y=float('inf'))

    def test_update_x_y_int_fail(self):
        """test x and y with integer that is less than 0
        """
        Base._Base__nb_objects = 0
        r1 = Square(10, 10, 10)
        self.assertEqual(str(r1), "[Square] (1) 10/10 - 10")

        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r1.update(1, 1, -1, 1)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r1.update(1, 1, 1, -1)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r1.update(1, 1, -1, -1)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r1.update(x=-1)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r1.update(y=-2)
        with self.assertRaises(ValueError):
            r1.update(y=-2, x=-1)

    def test_to_dictionary(self):
        """test to_dictionary medthod"""
        Base._Base__nb_objects = 0
        r1 = Square(2, 1, 9)
        r1_d = r1.to_dictionary()
        d = {'x': 1, 'y': 9, 'id': 1, 'size': 2}
        self.assertDictEqual(r1_d, d)
        self.assertEqual(type(r1_d), dict)
        r2 = Square(1, 1)
        r2.update(**r1_d)
        self.assertNotEqual(r1, r2)

    def test_to_dictionary_with_args(self):
        """test to dictionary with arguments"""
        r1 = Square(10, 2, 1, 9)
        with self.assertRaises(TypeError):
            r1.to_dictionary(1)
        with self.assertRaises(TypeError):
            r1.to_dictionary([1])
        with self.assertRaises(TypeError):
            r1.to_dictionary({1})
        with self.assertRaises(TypeError):
            r1.to_dictionary("s")
        with self.assertRaises(TypeError):
            r1.to_dictionary({'key': 1})
        with self.assertRaises(TypeError):
            r1.to_dictionary(1.2)
        with self.assertRaises(TypeError):
            r1.to_dictionary(True)
        with self.assertRaises(TypeError):
            r1.to_dictionary(False)
        with self.assertRaises(TypeError):
            r1.to_dictionary(None)
        with self.assertRaises(TypeError):
            r1.to_dictionary(float('nan'))
        with self.assertRaises(TypeError):
            r1.to_dictionary(float('inf'))
        with self.assertRaises(TypeError):
            r1.to_dictionary(1, 2)
if __name__ == '__main__':
    unittest.main()
