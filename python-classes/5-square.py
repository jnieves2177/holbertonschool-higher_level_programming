#!/usr/bin/python3
"""
Defines a class Square.
"""


class Square:
    """
    Represents a square.
    """

    def __init__(self, size=0):
        """
        Initializes a Square.
        Args:
        size: The size of the square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        """
        Obtain and set the current size of the square.
        """
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculates the area of the square and returns it.
        """
        return (self.__size ** 2)

    def my_print(self):
        """
        Print the square with '#'
        """
        for i in range(0, self.__size):
            [print("#", end="") for h in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")
