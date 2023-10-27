#!/usr/bin/python3
"""
Unittest for Square Class
# run with python3 -m unittest discover tests
# run with python3 -m unittest tests/test_models/test_square.py
"""

import unittest
import pep8
from io import StringIO
from contextlib import redirect_stdout
from models import square
Square = square.Square

class TestPep8(unittest.TestCase):
    """Pep8 models/square.py & tests/test_models/test_square.py"""

    def test_pep8(self):
        """Test PEP8 compliance"""
        style = pep8.StyleGuide(quiet=False)
        errors = 0
        files = ["models/square.py", "tests/test_models/test_square.py"]
        errors += style.check_files(files).total_errors
        self.assertEqual(errors, 0, 'Need to fix PEP8')

class TestSquare(unittest.TestCase):
    """Tests for models/square.py"""

    def setUp(self):
        # Common setup code, if needed for multiple test methods
        pass

    def test_attributes_given(self):
        """Test that all attributes match what's given"""
        s1 = Square(9, 99, 999, 1000)
        self.assertEqual(s1.width, 9)
        self.assertEqual(s1.height, 9)
        self.assertEqual(s1.size, 9)
        self.assertEqual(s1.x, 99)
        self.assertEqual(s1.y, 999)
        self.assertEqual(s1.id, 1000)

    def test_default_attributes(self):
        """Test that default attributes are set when not given"""
        s2 = Square(88)
        self.assertEqual(s2.width, 88)
        self.assertEqual(s2.height, 88)
        self.assertEqual(s2.size, 88)
        self.assertEqual(s2.x, 0)
        self.assertEqual(s2.y, 0)
        self.assertIsNotNone(s2.id)

    def test_attributes_validation(self):
        """Test that attributes are validated before set"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("10")
            Square([10, 3])
            Square({20, })
            Square({"d": 20})
            Square(None)
            Square((30, 20), 4)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(-1)
            Square(9).size(-9)

    # Add other test methods following a similar pattern

    def test_area(self):
        """Test method: area"""
        self.assertEqual(Square(3).area(), 9)
        self.assertEqual(Square(4, 0, 0).area(), 16)

    def test_display(self):
        """Test method: display"""
        with StringIO() as bufr, redirect_stdout(bufr):
            Square(4).display()
            b = bufr.getvalue()
        self.assertEqual(b, '####\n####\n####\n####\n')
        with StringIO() as bufr, redirect_stdout(bufr):
            Square(3, 1, 2).display()
            b = bufr.getvalue()
        self.assertEqual(b, '\n\n ###\n ###\n ###\n')

    def test_str(self):
        """Test method: __str__"""
        s = Square(1, 2, 3, 44)
        s.size = 500
        self.assertEqual(str(s), '[Square] (44) 2/3 - 500')

    def test_update_args(self):
        """Test method: update(*args)"""
        s = Square(1, 2, 3, 4)
        s.update(10, 10, 10, 10)
        self.assertEqual(str(s), '[Square] (10) 10/10 - 10')
        s.update()
        self.assertEqual(str(s), '[Square] (10) 10/10 - 10')
        s.update(99)
        self.assertEqual(str(s), '[Square] (99) 10/10 - 10')
        s.update(99, 5)
        self.assertEqual(str(s), '[Square] (99) 10/10 - 5')
        s.update(44, 55, 1, 2)
        self.assertEqual(str(s), '[Square] (44) 1/2 - 55')

    def test_update_kwargs(self):
        """Test method: update(**kwargs)"""
        s = Square(1, 2, 3, 4)
        s.update(id=88, size=77, nokey=99)
        self.assertEqual(str(s), '[Square] (88) 2/3 - 77')

    def test_to_dictionary(self):
        """Test method: to_dictionary"""
        sdic = Square(1, 2, 3, 4).to_dictionary()
        self.assertEqual(type(sdic), dict)
        s2 = Square(10, 10)
        s2.update(**sdic)
        self.assertEqual(str(s2), '[Square] (4) 2/3 - 1')
