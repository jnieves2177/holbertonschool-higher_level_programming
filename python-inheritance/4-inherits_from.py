#!/usr/bin/python3
"""
4-inherits_from.py
Defines an inherited class checking function.
"""


def inherits_from(obj, a_class):
    """
    Args:
        type() to get specific class
        isinstance() to get class and any parent classes too
        issubclass() to get what object is a subclass of

    Return:
        True if obj is instance of class that it inherits from or is subcls of
    """
    return (type(obj) is not a_class and issubclass(type(obj), a_class))
