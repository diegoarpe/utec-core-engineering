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
