#!/usr/bin/env python3
"""Module that defines the Square class, a subclass of Rectangle."""
Rectangle = __import__('2-rectangle').Rectangle


class Square(Rectangle):
    """Square defined by its side length."""

    def __init__(self, size):
        """Initialize a square with a validated side length."""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
