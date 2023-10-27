#!/usr/bin/python3
"""
Unittest for Rectangle Class
# Run with python3 -m unittest discover tests
# Run with python3 -m unittest tests/test_models/test_rectangle.py
"""

import os
import pep8
import unittest
from io import StringIO
from contextlib import redirect_stdout
from models import rectangle
Rectangle = rectangle.Rectangle

class TestPep8(unittest.TestCase):
    """Test PEP8 compliance for models/rectangle.py & tests/test_models/test_rectangle.py"""
    
    def test_pep8_compliance(self):
        """Check PEP8 compliance"""
        style = pep8.StyleGuide(quiet=False)
        errors = 0
        files = ["models/rectangle.py", "tests/test_models/test_rectangle.py"]
        errors += style.check_files(files).total_errors
        self.assertEqual(errors, 0, 'PEP8 compliance issues found')

class TestRectangleAttributes(unittest.TestCase):
    """Tests for attributes of the Rectangle class"""
    
    def test_all_attributes_given(self):
        """Test that all attributes match the values given"""
        r1 = Rectangle(10, 20, 1, 2, 99)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 20)
        self.assertEqual(r1.x, 1)
        self.assertEqual(r1.y, 2)
        self.assertEqual(r1.id, 99)

    def test_default_attributes(self):
        """Test default attributes are set when not given"""
        r2 = Rectangle(3, 4)
        self.assertEqual(r2.width, 3)
        self.assertEqual(r2.height, 4)
        self.assertEqual(r2.x, 0)
        self.assertEqual(r2.y, 0)
        self.assertIsNotNone(r2.id)

    # Add more attribute test cases following a similar pattern...

class TestRectangleMethods(unittest.TestCase):
    """Tests for methods of the Rectangle class"""
    
    def test_area(self):
        """Test the area method"""
        self.assertEqual(Rectangle(3, 4).area(), 12)
        self.assertEqual(Rectangle(8, 7, 0, 0).area(), 56)
        self.assertEqual(Rectangle(8, 7, 0, 0, 12).area(), 56)

    def test_display(self):
        """Test the display method"""
        with StringIO() as bufr, redirect_stdout(bufr):
            Rectangle(5, 3).display()
            b = bufr.getvalue()
        self.assertEqual(b, '#####\n#####\n#####\n')
        
        # Add more test cases for the display method...

    def test_str(self):
        """Test the __str__ method"""
        r = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(str(r), '[Rectangle] (5) 3/4 - 1/2')

    # Add more method test cases...

class TestRectangleUpdate(unittest.TestCase):
    """Tests for the update method of the Rectangle class"""

    def test_update_args(self):
        """Test the update method with positional arguments"""
        r = Rectangle(1, 2, 3, 4, 5)
        r.update(10, 10, 10, 10, 10)
        self.assertEqual(str(r), '[Rectangle] (10) 10/10 - 10/10')
        
        # Add more test cases for update with args...

    def test_update_kwargs(self):
        """Test the update method with keyword arguments"""
        r = Rectangle(1, 2, 3, 4, 5)
        r.update(id=55)
        self.assertEqual(str(r), '[Rectangle] (55) 3/4 - 1/2')

        # Add more test cases for update with kwargs...

    def test_mixture_of_valid_and_invalid_kwargs(self):
        """Test a mixture of valid and invalid keyword arguments in update"""
        r = Rectangle(1, 2, 3, 4, 5)
        r.update(nokey=1000, invalid=2000, testing=3000, id=4000)
        self.assertEqual(str(r), '[Rectangle] (4000) 3/4 - 1/2')

        # Add more test cases for mixture of valid and invalid kwargs...

class TestRectangleToDictionary(unittest.TestCase):
    """Tests for the to_dictionary method of the Rectangle class"""

    def test_to_dictionary(self):
        """Test the to_dictionary method"""
        rdic = Rectangle(1, 2, 3, 4, 5).to_dictionary()
        self.assertEqual(type(rdic), dict)
        
        r2 = Rectangle(10, 10)
        r2.update(**rdic)
        self.assertEqual(str(r2), '[Rectangle] (5) 3/4 - 1/2')

        # Add more test cases for to_dictionary...

if __name__ == '__main__':
    unittest.main()
