#!/usr/bin/python3
"""
9-rectangle.py
Defines a class Rectangle that inherits from BaseGeometry.
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Represents a rectangle using BaseGeometry.
    Methods:
        __init__(self, width, height)
        area(self)
        __str__
    """
    def __init__(self, width, height):
        """
        Validate and initialize width and height
        Args:
            width (int): private
            height (int): private
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """extends parent's empty method and returns area"""
        return self.__width * self.__height

    def __str__(self):
        """prints [Rectangle] <width>/<height>"""
        return "[{:s}] {:d}/{:d}".format(self.__class__.__name__,
                                         self.__width, self.__height)
