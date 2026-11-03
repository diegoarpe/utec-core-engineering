#!/usr/bin/env python3
"""Module that defines the Rectangle class, a subclass of BaseGeometry."""
BaseGeometry = __import__('base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle defined by its width and height."""

    def __init__(self, width, height):
        """Initialize a rectangle with a validated width and height."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Calculate the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Return the string description of the rectangle."""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
