#!/usr/bin/env python3
"""Module that defines the Rectangle class, derived from BaseGeometry."""
from base_geometry import BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle defined by its width and height."""

    def __init__(self, width, height):
        """Initialize a rectangle with a validated width and height."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Width of the rectangle."""
        return self.__width

    @property
    def height(self):
        """Height of the rectangle."""
        return self.__height
