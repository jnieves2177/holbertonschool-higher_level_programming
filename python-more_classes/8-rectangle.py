#!/usr/bin/python3
"""
Defines a Rectangle class.
"""


class Rectangle:
    """
    Represent a rectangle.

    Attributes:
       number_of_instances (int): The number of Rectangle instances.
       print_symbol (any): The symbol used for string representation.
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle.

        Args:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle.
        """
        type(self).number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Get the width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Set the width of the rectangle.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Get the height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Set the height of the rectangle.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Return the area of the Rectangle.
        """
        return (self.__width * self.__height)

    def perimeter(self):
        """
        Return the perimeter of the Rectangle.
        """
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Return the Rectangle with the greater area.

        Args:
            rect_1 (Rectangle): First Rectangle.
            rect_2 (Rectangle): Second Rectangle.
        Raises:
           TypeError: If either of shape_1 or shape_2 is not a Rectangle.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area:
            return (rect_1)
        return (rect_2)

    def __str__(self):
        """
        Return the print representation of the Rectangle.
        Represents the rectangle with the # character.
        """
        if self.__width == 0 or self.__height == 0:
            return ("")

        shape = []
        for i in range(self.__height):
            [shape.append(str(self.print_symbol)) for h in range(self.__width)]
            if i != self.__height - 1:
                shape.append("\n")
        return ("".join(shape))

    def __repr__(self):
        """
        Return the string representation of the Rectangle.
        """
        shape = "Rectangle(" + str(self.__width)
        shape += ", " + str(self.__height) + ")"
        return (shape)

    def __del__(self):
        """
        Print a message for every delete of a Rectangle.
        """
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
