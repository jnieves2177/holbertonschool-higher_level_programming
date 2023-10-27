#!/usr/bin/python3
"""
Unittest for Base Class
# Run with python3 -m unittest discover tests
# Run with python3 -m unittest tests/test_models/test_base.py
"""

import unittest
import pep8
import json
import os
from models import base
from models import rectangle
Base = base.Base
Rectangle = rectangle.Rectangle

class TestPep8(unittest.TestCase):
    """Pep8 models/base.py & tests/test_models/test_base.py"""

    def test_pep8(self):
        """Test code style with PEP8"""
        style = pep8.StyleGuide(quiet=False)
        errors = 0
        files = ["models/base.py", "tests/test_models/test_base.py"]
        errors += style.check_files(files).total_errors
        self.assertEqual(errors, 0, 'PEP8 style violations found')

class TestBase(unittest.TestCase):
    """Tests for models/base.py"""

    def setUp(self):
        """Set up for each test method"""
        self.base_instance = Base()

    def tearDown(self):
        """Clean up after each test method"""
        try:
            os.remove("Rectangle.json")
        except FileNotFoundError:
            pass

    def test_base_with_given_id(self):
        """Test IDs match when given"""
        self.assertEqual(Base(999).id, 999)
        self.assertEqual(Base(0).id, 0)
        self.assertEqual(Base(1).id, 1)
        self.assertEqual(Base(-80).id, -80)

    def test_base_with_incremented_id(self):
        """Test IDs match incremented nb_objects when not given"""
        self.assertEqual(self.base_instance.id, 1)
        self.assertEqual(Base().id, 2)

    def test_private_attr_access(self):
        """Test private attributes are not accessible"""
        with self.assertRaises(AttributeError):
            print(Base._Base__nb_objects)
            print(Base.nb_objects)

    def test_invalid_args(self):
        """Test too many args given throws error"""
        with self.assertRaises(TypeError):
            Base(50, 50)

    def test_class_creation(self):
        """Test class created is indeed Base"""
        self.assertIsInstance(self.base_instance, Base)

    def test_to_json_string(self):
        """Test dict given translates into JSON string"""
        test_dict = {"id": 1, "width": 2, "height": 3, "x": 4, "y": 5}
        json_string = Base.to_json_string([test_dict])
        self.assertTrue(isinstance(test_dict, dict))
        self.assertTrue(isinstance(json_string, str))
        self.assertEqual(json.loads(json_string), [test_dict])

    def test_none_to_json_string(self):
        """Test no dict given translates into JSON string of empty list"""
        self.assertEqual(Base.to_json_string([None]), "[]")

    def test_empty_to_json_string(self):
        """Test empty dict given translates into JSON string of empty list"""
        self.assertEqual(Base.to_json_string([{}]), "[]")

    def test_from_json_string(self):
        """Test JSON string translates into Python dict"""
        json_string = '[{"id": 1, "width": 2, "height": 3, "x": 4, "y": 5}]'
        python_dict = Base.from_json_string(json_string)
        self.assertTrue(isinstance(json_string, str))
        self.assertTrue(isinstance(python_dict, list))
        self.assertEqual(python_dict, [{"id": 1, "width": 2, "height": 3, "x": 4, "y": 5}])

    def test_from_none_json_string(self):
        """Test no JSON string translates into empty Python list"""
        self.assertEqual(Base.from_json_string(None), [])

    def test_from_empty_json_string(self):
        """Test empty JSON string translates into empty Python list"""
        self.assertEqual(Base.from_json_string(""), [])

    def test_create_instance_from_dictionary(self):
        """Test transferring attribute dictionary to another instance"""
        r = Rectangle(3, 5, 1, 2, 99)
        rdic = r.to_dictionary()
        r2 = Rectangle.create(**rdic)
        self.assertEqual(str(r), '[Rectangle] (99) 1/2 - 3/5')
        self.assertEqual(str(r2), '[Rectangle] (99) 1/2 - 3/5')
        self.assertIsNot(r, r2)

    def test_save_to_file(self):
        """Test save to file"""
        r = Rectangle(10, 7, 2, 8, 99)
        r2 = Rectangle(2, 4, 2, 2, 98)
        Rectangle.save_to_file([r, r2])
        with open("Rectangle.json", "r") as file:
            self.assertEqual(json.loads(file.read()), [r.to_dictionary(), r2.to_dictionary()])

    def test_save_none_to_file(self):
        """Test save None to file"""
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(), "[]")

    def test_save_empty_list_to_file(self):
        """Test save empty list to file"""
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(), "[]")

    def test_load_from_file(self):
        """Test load from file"""
        r = Rectangle(10, 7, 2, 8, 99)
        r2 = Rectangle(2, 4, 2, 2, 98)
        Rectangle.save_to_file([r, r2])
        recs = Rectangle.load_from_file()
        self.assertEqual(len(recs), 2)
        self.assertEqual(str(recs[0]), '[Rectangle] (99) 2/8 - 10/7')
        self.assertEqual(str(recs[1]), '[Rectangle] (98) 2/2 - 2/4')

    def test_load_from_none_file(self):
        """Test load from None file"""
        Rectangle.save_to_file(None)
        recs = Rectangle.load_from_file()
        self.assertEqual(recs, [])

    def test_load_from_empty_file(self):
        """Test load from empty file"""
        Rectangle.save_to_file([])
        recs = Rectangle.load_from_file()
        self.assertEqual(recs, [])
