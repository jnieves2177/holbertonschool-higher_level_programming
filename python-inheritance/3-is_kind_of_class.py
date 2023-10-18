#!/usr/bin/python3
"""
3-is_kind_of_class.py

Defines a class and inherited class checking function.
"""


def is_kind_of_class(obj, a_class):
    """
    Args:
        use type() to get specific class
        use isinstance() to get class and any parent classes too
        use issubclass() to get what object is a subclass of

    Return:
        True if obj is an instance of class that it inherited from
    """
    return isinstance(obj, a_class)
