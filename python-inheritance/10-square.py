#!/usr/bin/python3
"""
10-square.py
Defines a Rectangle subclass Square
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Inherits from Rectangle, who inherits from BaseGeometry
    Methods:
        __init__(self, size)
    """
    def __init__(self, size):
        """initializes size
        Args:
            size (int): private
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
